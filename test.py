import streamlit as st
ni= st.number_input('Enter(Number_input)', step = 0.5)
if (ni-int(ni)== 0):
    ni = int(ni)
st.write(ni)



# import pymongo
# client = pymongo.MongoClient(
#             "mongodb+srv://admin:pavilion15@cluster0.pefyq.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
# db = client['ResumeData']
# col = db['resumes']
#
# col.delete_many({})
#
# find = col.find()
# master = []
# for i in find:
#     # all = (i['Skill'])
#     # for j in all:
#     #     master.append(j[1].lower())
#     print(i['Skill'][0][0])
# print(list(set(master)))
#


# from docx2python import docx2python
# import pandas as pd
# def flatten_df(df):
#     db = df
#     for i in range(len(df.columns)):
#         for j in range(len(df[i])):
#             db[i][j] = df[i][j][0][0]
#     return db
#
# def get_info(file):
#     document = docx2python(file)
#     d = dict()
#     l = flatten_df(pd.DataFrame(document.body_runs[1]))
#     for i in range(len(l[0])):
#         l[1][i] = l[1][i].lower()
#     l.loc[l[0] == 'Years of Experience', 1].iloc[0] = float(l.loc[l[0] == 'Years of Experience', 1].iloc[0])
#     d['personal_info_df'] = l
#     d['summary_list'] = ((document.body_runs[2])[0][0][2:])
#     t = flatten_df(pd.DataFrame(document.body_runs[3]))
#     for i in range(len(t[0])):
#         t[0][i] = t[0][i].lower()
#     d['skills_df'] = t
#     d['domain'] = (document.body_runs[4][0][0][2])
#     # d['project_df'] = flatten_df(pd.DataFrame(document.body_runs[5]))
#     d['education_df'] = flatten_df(pd.DataFrame(document.body_runs[9]))
#     d['certification_list'] = (document.body_runs[10][0][0][2:])
#     d['visa_df'] = flatten_df(pd.DataFrame(document.body_runs[11]).drop(2, axis=1))
#     d['link'] = str(document.body_runs[12][0][0][1][0])  #[9:-4]
#     return d
#
#
# u = get_info('SAMPLE RESUME.docx')
#
# print(u['personal_info_df'].info())

# p = pd.concat([u['personal_info_df'], u['skills_df'], u['education_df'], u['visa_df']])
# dt = pd.Series(['status', 'Unassigned'], index=p.columns)
# p = p.append(dt, ignore_index=True)
# l = pd.Series(['link', u['link']], index=p.columns)
# p = p.append(l, ignore_index=True)
# skill = []
# for i in range(len(u['skills_df'][0])):
#     o = []
#     o.append(u['skills_df'][0][i])
#     o.append(u['skills_df'][1][i])
#     skill.append(o)
# sl = pd.Series(['Skill', skill], index=p.columns)
# p = p.append(sl, ignore_index=True)
# dic_list = dict(p.values)
# print(p)
# # for i in range(len(list(p['OHR ID']))):
# # view = col.find_one({'OHR ID': p[1][1]})
# # if view == None:
# #     col.insert_one(dic_list)

# print(u['skills_df'])



# master = []
# find = col.find()
# for i in find:
#     all = (i['Skill'])
#     for j in all:
#         master.append(j[0])
# skill = list(set(master))
# count = []
# for i in range(len(skill)):
#     count.append(master.count(skill[i]))
# sd = pd.DataFrame(columns=['skill', 'count'])
# sd['skill'] = skill
# sd['count'] = count
# print(sd)





