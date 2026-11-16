import csv
from collections import defaultdict

csv_path = r'C:\Users\viyass\Downloads\6af855c0e8386_ball_by_ball.csv'

batters = defaultdict(lambda: {
    'balls': 0, 'runs': 0, 'fours': 0, 'sixes': 0, 'dots': 0, 'dismissals': 0,
    'pp_balls': 0, 'pp_runs': 0, 'pp_outs': 0,
    'mid_balls': 0, 'mid_runs': 0, 'mid_outs': 0,
    'death_balls': 0, 'death_runs': 0, 'death_outs': 0,
    'pace_balls': 0, 'pace_runs': 0, 'pace_outs': 0,
    'spin_balls': 0, 'spin_runs': 0, 'spin_outs': 0,
    'inns2_balls': 0, 'inns2_runs': 0, 'inns2_outs': 0,
    'batting_type': '', 'matches': set()
})

bowlers = defaultdict(lambda: {
    'legal_balls': 0, 'runs_conceded': 0, 'wickets': 0, 'dots': 0,
    'fours': 0, 'sixes': 0, 'wides': 0, 'noballs': 0,
    'pp_balls': 0, 'pp_runs': 0, 'pp_wickets': 0,
    'mid_balls': 0, 'mid_runs': 0, 'mid_wickets': 0,
    'death_balls': 0, 'death_runs': 0, 'death_wickets': 0,
    'bowling_type': '', 'pace_spin': '', 'matches': set()
})

with open(csv_path, 'r', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    for row in reader:
        m_id = row['match_id']
        inns = int(row['innings']) if row['innings'].isdigit() else 1
        if inns not in (1, 2):
            continue
        
        over = int(row['overid']) if row['overid'].isdigit() else 1
        bat_name = row['striker_name']
        bowl_name = row['bowler_name']
        bat_type = row['batting_type']
        bowl_type = row['bowling_type']
        pace_spin = row['pace_or_spin']
        
        runs = int(row['runs']) if row['runs'].lstrip('-').isdigit() else 0
        extra_type = row['extras_type']
        e1 = int(row['extras1_runs']) if row['extras1_runs'].isdigit() else 0
        e2 = int(row['extras_2_runs']) if row['extras_2_runs'].isdigit() else 0
        is_four = row['is_four'].lower() == 'true'
        is_six = row['is_six'].lower() == 'true'
        is_wkt = row['is_wicket'].lower() == 'true'
        dismissal = row['dismissal_type']
        
        is_legal = extra_type not in ('wide', 'Overstep')
        is_wide = extra_type == 'wide'
        is_noball = extra_type == 'Overstep'
        
        # Batting stats (legal deliveries faced by striker, or runs off no-ball)
        if extra_type != 'wide':
            b = batters[bat_name]
            b['balls'] += 1
            b['runs'] += runs
            if runs == 0 and not is_four and not is_six:
                b['dots'] += 1
            if is_four:
                b['fours'] += 1
            if is_six:
                b['sixes'] += 1
            if is_wkt and row['dismissed_player_id'] == row['striker_id']:
                b['dismissals'] += 1
            if bat_type and not b['batting_type']:
                b['batting_type'] = bat_type
            b['matches'].add(m_id)
            
            # Phase
            if over <= 6:
                b['pp_balls'] += 1
                b['pp_runs'] += runs
                if is_wkt and row['dismissed_player_id'] == row['striker_id']:
                    b['pp_outs'] += 1
            elif over <= 15:
                b['mid_balls'] += 1
                b['mid_runs'] += runs
                if is_wkt and row['dismissed_player_id'] == row['striker_id']:
                    b['mid_outs'] += 1
            else:
                b['death_balls'] += 1
                b['death_runs'] += runs
                if is_wkt and row['dismissed_player_id'] == row['striker_id']:
                    b['death_outs'] += 1
                    
            # Pace vs Spin
            if pace_spin == 'Pace':
                b['pace_balls'] += 1
                b['pace_runs'] += runs
                if is_wkt and row['dismissed_player_id'] == row['striker_id']:
                    b['pace_outs'] += 1
            elif pace_spin == 'Spin':
                b['spin_balls'] += 1
                b['spin_runs'] += runs
                if is_wkt and row['dismissed_player_id'] == row['striker_id']:
                    b['spin_outs'] += 1
                    
            # Inns 2 (Chase)
            if inns == 2:
                b['inns2_balls'] += 1
                b['inns2_runs'] += runs
                if is_wkt and row['dismissed_player_id'] == row['striker_id']:
                    b['inns2_outs'] += 1

        # Bowling stats
        bw = bowlers[bowl_name]
        bw['matches'].add(m_id)
        if bowl_type and not bw['bowling_type']:
            bw['bowling_type'] = bowl_type
        if pace_spin and not bw['pace_spin']:
            bw['pace_spin'] = pace_spin
            
        bowler_runs = runs
        if is_wide:
            bowler_runs += max(1, e1 + e2)
            bw['wides'] += 1
        elif is_noball:
            bowler_runs += max(1, e1 + e2)
            bw['noballs'] += 1
            
        bw['runs_conceded'] += bowler_runs
        
        if is_legal:
            bw['legal_balls'] += 1
            if bowler_runs == 0:
                bw['dots'] += 1
            if is_four:
                bw['fours'] += 1
            if is_six:
                bw['sixes'] += 1
                
        # Bowler wicket (exclude run out / retired)
        if is_wkt and dismissal not in ('Run Out', 'Retired Hurt', 'Retired Out', 'Obstructing the field', 'Handled the ball'):
            bw['wickets'] += 1
            
        # Bowler phase
        if is_legal:
            if over <= 6:
                bw['pp_balls'] += 1
                bw['pp_runs'] += bowler_runs
                if is_wkt and dismissal not in ('Run Out', 'Retired Hurt'):
                    bw['pp_wickets'] += 1
            elif over <= 15:
                bw['mid_balls'] += 1
                bw['mid_runs'] += bowler_runs
                if is_wkt and dismissal not in ('Run Out', 'Retired Hurt'):
                    bw['mid_wickets'] += 1
            else:
                bw['death_balls'] += 1
                bw['death_runs'] += bowler_runs
                if is_wkt and dismissal not in ('Run Out', 'Retired Hurt'):
                    bw['death_wickets'] += 1

print(f"Processed {len(batters)} batters and {len(bowlers)} bowlers.")

# Filter and format batters (min 60 balls faced)
batter_rows = []
for name, data in batters.items():
    if data['balls'] < 60:
        continue
    sr = round((data['runs'] / data['balls']) * 100, 1)
    bpd = round(data['balls'] / max(1, data['dismissals']), 1)
    dot_pct = round((data['dots'] / data['balls']) * 100, 1)
    boundary_pct = round(((data['fours'] + data['sixes']) / data['balls']) * 100, 1)
    
    pp_sr = round((data['pp_runs'] / max(1, data['pp_balls'])) * 100, 1) if data['pp_balls'] >= 10 else 0
    mid_sr = round((data['mid_runs'] / max(1, data['mid_balls'])) * 100, 1) if data['mid_balls'] >= 10 else 0
    death_sr = round((data['death_runs'] / max(1, data['death_balls'])) * 100, 1) if data['death_balls'] >= 10 else 0
    
    pace_sr = round((data['pace_runs'] / max(1, data['pace_balls'])) * 100, 1) if data['pace_balls'] >= 10 else 0
    spin_sr = round((data['spin_runs'] / max(1, data['spin_balls'])) * 100, 1) if data['spin_balls'] >= 10 else 0
    chase_sr = round((data['inns2_runs'] / max(1, data['inns2_balls'])) * 100, 1) if data['inns2_balls'] >= 10 else 0
    
    death_share = round((data['death_balls'] / data['balls']) * 100, 1)
    pp_share = round((data['pp_balls'] / data['balls']) * 100, 1)
    mid_share = round((data['mid_balls'] / data['balls']) * 100, 1)
    
    batter_rows.append({
        'Player': name,
        'Batting_Type': data['batting_type'] or 'RHB',
        'Matches': len(data['matches']),
        'Balls_Faced': data['balls'],
        'Runs_Scored': data['runs'],
        'Strike_Rate': sr,
        'Balls_Per_Dismissal': bpd,
        'Dismissals': data['dismissals'],
        'Fours': data['fours'],
        'Sixes': data['sixes'],
        'Dot_Pct': dot_pct,
        'Boundary_Pct': boundary_pct,
        'PP_Balls': data['pp_balls'],
        'PP_SR': pp_sr,
        'PP_Share_Pct': pp_share,
        'Mid_Balls': data['mid_balls'],
        'Mid_SR': mid_sr,
        'Mid_Share_Pct': mid_share,
        'Death_Balls': data['death_balls'],
        'Death_SR': death_sr,
        'Death_Share_Pct': death_share,
        'Pace_Balls': data['pace_balls'],
        'Pace_SR': pace_sr,
        'Spin_Balls': data['spin_balls'],
        'Spin_SR': spin_sr,
        'Chase_Balls': data['inns2_balls'],
        'Chase_SR': chase_sr
    })

batter_rows.sort(key=lambda x: x['Balls_Faced'], reverse=True)

# Write batters universe
with open('data/Full_Batters_Universe_2022_2026.csv', 'w', newline='', encoding='utf-8') as f:
    writer = csv.DictWriter(f, fieldnames=list(batter_rows[0].keys()))
    writer.writeheader()
    writer.writerows(batter_rows)
print(f"Exported {len(batter_rows)} batters to data/Full_Batters_Universe_2022_2026.csv")

# Filter and format bowlers (min 60 legal balls bowled)
bowler_rows = []
for name, data in bowlers.items():
    if data['legal_balls'] < 60:
        continue
    econ = round((data['runs_conceded'] / data['legal_balls']) * 6.0, 2)
    bpw = round(data['legal_balls'] / max(1, data['wickets']), 1)
    dot_pct = round((data['dots'] / data['legal_balls']) * 100, 1)
    
    pp_econ = round((data['pp_runs'] / max(1, data['pp_balls'])) * 6.0, 2) if data['pp_balls'] >= 10 else 0
    mid_econ = round((data['mid_runs'] / max(1, data['mid_balls'])) * 6.0, 2) if data['mid_balls'] >= 10 else 0
    death_econ = round((data['death_runs'] / max(1, data['death_balls'])) * 6.0, 2) if data['death_balls'] >= 10 else 0
    
    death_share = round((data['death_balls'] / data['legal_balls']) * 100, 1)
    pp_share = round((data['pp_balls'] / data['legal_balls']) * 100, 1)
    mid_share = round((data['mid_balls'] / data['legal_balls']) * 100, 1)
    
    bowler_rows.append({
        'Player': name,
        'Bowling_Type': data['bowling_type'],
        'Pace_Spin': data['pace_spin'],
        'Matches': len(data['matches']),
        'Overs_Bowled': round(data['legal_balls'] / 6.0, 1),
        'Legal_Balls': data['legal_balls'],
        'Runs_Conceded': data['runs_conceded'],
        'Wickets': data['wickets'],
        'Economy': econ,
        'Balls_Per_Wicket': bpw,
        'Dot_Pct': dot_pct,
        'PP_Balls': data['pp_balls'],
        'PP_Econ': pp_econ,
        'PP_Wickets': data['pp_wickets'],
        'PP_Share_Pct': pp_share,
        'Mid_Balls': data['mid_balls'],
        'Mid_Econ': mid_econ,
        'Mid_Wickets': data['mid_wickets'],
        'Mid_Share_Pct': mid_share,
        'Death_Balls': data['death_balls'],
        'Death_Econ': death_econ,
        'Death_Wickets': data['death_wickets'],
        'Death_Share_Pct': death_share
    })

bowler_rows.sort(key=lambda x: x['Legal_Balls'], reverse=True)

with open('data/Full_Bowlers_Universe_2022_2026.csv', 'w', newline='', encoding='utf-8') as f:
    writer = csv.DictWriter(f, fieldnames=list(bowler_rows[0].keys()))
    writer.writeheader()
    writer.writerows(bowler_rows)
print(f"Exported {len(bowler_rows)} bowlers to data/Full_Bowlers_Universe_2022_2026.csv")
