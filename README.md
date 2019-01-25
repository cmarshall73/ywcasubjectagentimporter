# ywcasubjectagentimporter

# Create Files
1. Open YWCA spreadsheet and download each sheet (predandmin, local, subfiles)
2. Using Open Refine, convert each sheet into a JSON object

# Run Program
1. Run corporate_agents.py twice
    1. First - ‘yes’ - to query 
    2. Second - ‘cache’ - to add agents
2. Run people_agents.py twice
    1. First - ‘yes’ - to query
    2. Second - ‘cache’ - to add agents
3. Run all_subs.py twice
    1. First ‘yes’ - to query
    2. Second - ‘cache’ - to add subjects
4. Run missing_subjects_agents.py
5. Run ywca_agent_subject_add.py on each of the three files (predandmin.json, local.json, subfiles.json) python3 ywca_agent_subject_add.py predandmin.json prod 
