import sqlite3
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


def convert():  
    data = pd.read_csv("Copy of spine biopsy data.csv") #uses panda to read the csv file. 
    data.to_sql("joey_data", con = sqlite3.connect("joey_data.db"),if_exists='append', index = False)



def avg_weight():
    con = sqlite3.connect("joey_data.db")
    cur = con.cursor()

    output_1 = cur.execute('SELECT AVG( "Weight (kg)") FROM joey_data WHERE "Included or Excluded" = "Included" AND Sex = "Male"')
    ouu = output_1.fetchall()

    output_2 = cur.execute('SELECT AVG( "Weight (kg)") FROM joey_data WHERE "Included or Excluded" = "Included" AND Sex = "Female"')
    moe = output_2.fetchall()

    print(ouu)
    # print("BALLLLLS")
    print(moe)


def number_of_patients():
    con = sqlite3.connect("joey_data.db")
    cur = con.cursor()
    output_1 = cur.execute('SELECT COUNT(*) FROM joey_data WHERE "Included or Excluded" = "Included"')
    ouu = output_1.fetchall()
    
    print(ouu)
     
def did_biopsy_matter():
    con = sqlite3.connect("joey_data.db")
    cur = con.cursor()

    How_many_were_no = cur.execute('SELECT COUNT("Antibiotics influenced by biopsy?") FROM joey_data WHERE "Included or Excluded" = "Included" AND "Antibiotics influenced by biopsy?" LIKE "%No%"')
    ## 63 patients did not change antibotic course after biospy.
    No_tings = How_many_were_no.fetchall()

    How_many_were_yes = cur.execute('SELECT COUNT("Antibiotics influenced by biopsy?") FROM joey_data WHERE "Included or Excluded" = "Included" AND "Antibiotics influenced by biopsy?" = "Yes"')
    Yes_tings = How_many_were_yes.fetchall()
    ## 15 patients did not change their antibotic course after biospy.

    similar = cur.execute('SELECT COUNT("Antibiotics influenced by biopsy?") FROM joey_data WHERE "Included or Excluded" = "Included" AND "Antibiotics influenced by biopsy?" = "Very similar antibiotics"')
    ouu3 = similar.fetchall()

    maybe_t = cur.execute('SELECT COUNT("Antibiotics influenced by biopsy?") FROM joey_data WHERE "Included or Excluded" = "Included" AND "Antibiotics influenced by biopsy?" LIKE "%maybe%"')
    maybee = maybe_t.fetchall()

    print(ouu3)

def make_first_chart():
    y = np.array([63,7,16, 2, 2])
    my_labels = ['Biopsy Did Not Affect Antibotic Protocol', 'Maybe (bacteremia/prior yeast/TB/UTI/PBC', 'Biospy Did Affect Antibotic Protocol', "Very similar antibiotics", "Changed before cultures came back"]

    myexplode = [0.2, 0, 0, 0, 0]
    plt.pie(y, labels = my_labels,autopct='%1.0f%%', explode = myexplode,)
    plt.savefig("firstchart.png", bbox_inches = "tight", dpi=300)
    plt.show() 


def did_bmi_affect_biopsy_data():
    con = sqlite3.connect("joey_data.db")
    cur = con.cursor()

    count = cur.execute('SELECT COUNT(BMI) FROM joey_data WHERE "Included or Excluded" = "Included" AND "Antibiotics influenced by biopsy?" LIKE "%No%" AND BMI > 35')
    countt = count.fetchall()
    print(countt)






def show_bmi_chart():
    labels = ['Less than 18.5', '18.5-24.9', '25-29.9', '30-34.9', 'Greater than 35']
    yes_means = [0, 5, 8, 5, 5,]
    no_means =  [2, 16, 10, 12, 18,]

    x = np.arange(len(labels))  # the label locations
    width = 0.35  # the width of the bars

    fig, ax = plt.subplots()
    rects1 = ax.bar(x - width/2, yes_means, width, label='Protocol did Change')
    rects2 = ax.bar(x + width/2, no_means, width, label='Protocol did not Change')

    # Add some text for labels, title and custom x-axis tick labels, etc.
    
    ax.set_xlabel('BMI Ranges')
    ax.set_ylabel("Number of Patients")
    ax.set_title('BMI Relationship to Change in Protocol')
    ax.set_xticks(x, labels)
    ax.legend(bbox_to_anchor=(1.04, 1), loc="upper left")

    ax.bar_label(rects1, padding=3)
    ax.bar_label(rects2, padding=3)

    fig.tight_layout()
    plt.savefig("second.png", bbox_inches = "tight", dpi=300)
    plt.show()


def left_or_right_data():
    con = sqlite3.connect("joey_data.db")
    cur = con.cursor()

    leftI = cur.execute('SELECT COUNT("Right or left approach") FROM joey_data WHERE "Included or Excluded" = "Included" AND "Right or left approach" LIKE "%left%" AND "Antibiotics influenced by biopsy?" LIKE "%No%"  ')
    leftO = leftI.fetchall()
    print(leftO)
    # 51 out of 70 patients did not change their protocol. of those 51:
    ##24 patients did not change their protocol when on left method
    #27 patients did not change their protocol when on right method 

    #19 out of 70 patients did change their protocol, of those 19:
    #13 patients changed their protocal when on right method
    #6 patients changed their protocol when on left method
    

    #2 left and 2right both were on similar medication

def left_or_right_graph():
   

    labels = ['Left Approach', 'Right Approach',]
    yes_means = [6, 13,]
    no_means = [24, 27,]  

    x = np.arange(len(labels))  # the label locations
    width = 0.35  # the width of the bars

    fig, ax = plt.subplots()
    rects1 = ax.bar(x - width/2, yes_means, width, label='Protocol Changed')
    rects2 = ax.bar(x + width/2, no_means, width, label='Protocol did not Change')

    # Add some text for labels, title and custom x-axis tick labels, etc.
    ax.set_ylabel('Number of Patients')
    ax.set_xlabel('Method')
    ax.set_title('Effect of Left or Right method on Protocol Change')
    ax.set_xticks(x, labels)
    ax.legend(bbox_to_anchor=(1.04, 1), loc="upper left")

    ax.bar_label(rects1, padding=3)
    ax.bar_label(rects2, padding=3)

    fig.tight_layout()
    plt.savefig("lefotOrRight.png", bbox_inches = "tight", dpi=300)
    plt.show()

def number_of_passes_data():
    con = sqlite3.connect("joey_data.db")
    cur = con.cursor()
    
    passes = cur.execute('SELECT COUNT("Number of passes") FROM joey_data WHERE "Included or Excluded" = "Included" AND "Antibiotics influenced by biopsy?" LIKE "%Very%" AND "Number of passes" = "4" ')
    npasses = passes.fetchall()
    print(npasses)

    #10 patients changed their protocol after 1 pass
    #2 patients changed their protocol after 2 passes
    #4 patients changed their protocol after 3 passes
    #3 patients changed their protocol after 4 passes
    # 0 patients changed their protocol after more than 4 passes

    #22 patients did not changed their protocol after 1 pass
    #19 patients did not change their protocol after 2 passes
    #2 patients did not change their protocol after 3 passes
    #2 patients did not change their protocol after 4 passes
    #4 patients did not change their protocol after multiple passes
def number_of_passes_graph():
    labels = ['1 Pass', '2 Passes', '3 Passes', '4 Passes', 'More than 4 Passes']
    yes_means = [10, 2, 4, 3, 0]
    no_means = [22, 19, 2, 2, 4]  

    x = np.arange(len(labels))  # the label locations
    width = 0.35  # the width of the bars

    fig, ax = plt.subplots()
    rects1 = ax.bar(x - width/2, yes_means, width, label='Protocol Changed')
    rects2 = ax.bar(x + width/2, no_means, width, label='Protocol did not Change')

    # Add some text for labels, title and custom x-axis tick labels, etc.
    ax.set_ylabel('Number of Patients')
    ax.set_xlabel('Number of Passes')
    ax.set_title('Effect of # of Passes on Protocol Change')
    ax.set_xticks(x, labels)
    ax.legend()

    ax.bar_label(rects1, padding=3)
    ax.bar_label(rects2, padding=3)

    fig.tight_layout()
    plt.savefig("passes.png", bbox_inches = "tight", dpi=300)
    plt.show()


def specimen_type():
    con = sqlite3.connect("joey_data.db")
    cur = con.cursor()


    specify = cur.execute('SELECT COUNT("Specimen obtained (bone, disc, soft tissue, fluid, etc)") FROM joey_data WHERE "Included or Excluded" = "Included" AND "Specimen obtained (bone, disc, soft tissue, fluid, etc)" = "blood, bone" AND "Antibiotics influenced by biopsy?" LIKE "%No%" ')
    specifyList = specify.fetchall()

    df  = pd.read_csv("Copy of spine biopsy data.csv", encoding='latin-1')
    colList = df["Specimen obtained (bone, disc, soft tissue, fluid, etc)"].value_counts()
    #colList.to_excel("specimen.xlsx")

    print(specifyList)


def show_specimen_graph():
    labels = ['Bone', 'Fluid', 'Soft tissue']
    yes_means = [6, 4, 3,]
    no_means = [9, 12, 10 ]

    x = np.arange(len(labels))  # the label locations
    width = 0.35  # the width of the bars

    fig, ax = plt.subplots()
    rects1 = ax.bar(x - width/2, yes_means, width, label='Protocol Changed')
    rects2 = ax.bar(x + width/2, no_means, width, label='Protocol did not Change')

    # Add some text for labels, title and custom x-axis tick labels, etc.
    ax.set_ylabel('Number of Patients')
    ax.set_xlabel('Type of Specimen')
    ax.set_title('Effect of Single Specimen on Protocol Change')
    ax.set_xticks(x, labels)
    ax.legend()

    ax.bar_label(rects1, padding=3)
    ax.bar_label(rects2, padding=3)

    fig.tight_layout()
    plt.savefig("fifthssss.png", bbox_inches = "tight", dpi=300)
    plt.show()



def show_specimen_graph2():
    labels = ['Bone and Fluid', 'Bone and Soft tissue', 'Fluid and Soft tissue', 'Bone, Soft Tissue, and Fluid']
    yes_means = [6, 4, 1,1]
    no_means = [17, 11, 2,3 ]

    x = np.arange(len(labels))  # the label locations
    width = 0.35  # the width of the bars

    fig, ax = plt.subplots()
    rects1 = ax.bar(x - width/2, yes_means, width, label='Protocol Changed')
    rects2 = ax.bar(x + width/2, no_means, width, label='Protocol did not Change')

    # Add some text for labels, title and custom x-axis tick labels, etc.
    ax.set_ylabel('Number of Patients')
    ax.set_title('Effect of Combined Specimen on Protocol Change')
    ax.set_xticks(x, labels)
    ax.legend()

    ax.bar_label(rects1, padding=3)
    ax.bar_label(rects2, padding=3)

    fig.tight_layout()
    fig.autofmt_xdate()
    plt.savefig("fifth2.png", bbox_inches = "tight", dpi=300)
    plt.show()


def Radiologists():
    con = sqlite3.connect("joey_data.db")
    cur = con.cursor()
    find_names = cur.execute('SELECT COUNT("Radiologist name") FROM joey_data WHERE "Included or Excluded" = "Included" AND "Antibiotics influenced by biopsy?" LIKE "%No%" AND "Radiologist name" = "Dr. Patel"')

    names = find_names.fetchall()
    print(names)



    df  = pd.read_csv("Copy of spine biopsy data.csv", encoding='latin-1')
    colList = df["Radiologist name"].value_counts()
    #colList.to_excel("radioMEN.xlsx")
    #print(colList)

def radiologist_graph():
    labels = ['Dr. David Pasquale', 'Albert Song', 'Anup Alexander', 'Laurie Lomasney', 'Emad Allam', 'Dr. Rina Patel' ]
    yes_means = [5, 7, 7,4,1,1]
    no_means = [16, 18, 7, 14,5, 3]

    x = np.arange(len(labels))  # the label locations
    width = 0.35  # the width of the bars

    fig, ax = plt.subplots()
    rects1 = ax.bar(x - width/2, yes_means, width, label='Protocol Changed')
    rects2 = ax.bar(x + width/2, no_means, width, label='Protocol did not Change')

    # Add some text for labels, title and custom x-axis tick labels, etc.
    ax.set_ylabel('Number of Patients')
    ax.set_xlabel('Name of Radiologist')
    ax.set_title("Patients' Radiologist vs Protocol Changes")
    ax.set_xticks(x, labels)
    ax.legend()

    ax.bar_label(rects1, padding=3)
    ax.bar_label(rects2, padding=3)

    fig.tight_layout()
    fig.autofmt_xdate()
    plt.savefig("sixth.png", bbox_inches = "tight", dpi=300)
    plt.show()


def find_residents():
   # df  = pd.read_csv("Copy of spine biopsy data.csv", encoding='latin-1')
   # colList = df["Resident / other involvement"].value_counts()
   # colList.to_excel("residents.xlsx")

    con = sqlite3.connect("joey_data.db")
    cur = con.cursor()
    find_residents = cur.execute('SELECT COUNT("Resident / other involvement") FROM joey_data WHERE "Included or Excluded" = "Included" AND "Antibiotics influenced by biopsy?" LIKE "%changed%"')

    found_res = find_residents.fetchall()
    print(found_res)


def residents_graph():


    # Setting labels for items in Chart
    Employee = ['Protocol Changed', 'Protocol did not Change']

    # Setting size in Chart based on
    # given values
    Salary = [10, 42,]

    # colors
    colors = ['#ADFF2F', '#FF0000'] #ADFF2F
    # explosion
    explode = (0.05, 0.05,)

    # Pie Chart
    plt.pie(Salary, colors=colors, labels=Employee,
            autopct='%1.1f%%', pctdistance=0.85,
            explode=explode)

    # draw circle
    centre_circle = plt.Circle((0, 0), 0.70, fc='white')
    fig = plt.gcf()

    # Adding Circle in Pie chart
    fig.gca().add_artist(centre_circle)

    # Adding Title of chart
    plt.title('Effect of residents on Protocol change')

    # Displaying Chart
    fig.tight_layout()
    fig.autofmt_xdate()
    plt.savefig("residents_graph.png", bbox_inches = "tight", dpi=300)
    plt.show()


def back_pain():

    df  = pd.read_csv("Copy of spine biopsy data.csv", encoding='latin-1')
    colList = df["Back pain"].value_counts()
   # colList.to_excel("backpain.xlsx")



    con = sqlite3.connect("joey_data.db")
    cur = con.cursor()
    find_back_pain = cur.execute('SELECT COUNT("Back pain") FROM joey_data WHERE "Included or Excluded" = "Included" AND "Back pain" LIKE "%No%" AND "Antibiotics influenced by biopsy?" LIKE "%yes%"  ')
    back_painting = find_back_pain.fetchall()
    print(back_painting)

def back_pain_graph():
   

    # Data for the first donut chart
    data1 = [26, 59]
    labels1 = ['Did change antibotic protocol', 'Did not change antibotic protocol' ]

    # Data for the second donut chart
    data2 = [4,]
    labels2 = ['Did not change antibotic protocol']

    # Create the figure and the subplots
    fig, ax1, = plt.subplots()

    # Create the first donut chart
    ax1.pie(data1, labels=labels1, autopct='%1.1f%%', startangle=90)
    ax1.set(aspect="equal", title='Patients who had back pain')

    # Create the second donut chart
   

    # Show the plot
    plt.savefig("back_pain_graph.png", bbox_inches = "tight", dpi=300)
    plt.show()

   

def fever_data():
    con = sqlite3.connect("joey_data.db")
    cur = con.cursor()
    find_fever = cur.execute('SELECT COUNT("Fever") FROM joey_data WHERE "Included or Excluded" = "Included" AND "Fever" LIKE "%Yes%" AND "Antibiotics influenced by biopsy?" LIKE "%No%" ')
    found_fever = find_fever.fetchall()
    print(found_fever)



def fever_graph():
    

    
  
    # Data for the first donut chart
    data1 = [3, 5, ]
    labels1 = ['Changed Protocol', 'Did not change Protocol',]
# Data for the second donut chart
    data2 = [23, 58,]
    labels2 = ['Changed Protocol', 'Did not change Protocol', ]

# Create the first donut chart
    fig, ax = plt.subplots()
    ax.pie(data1, labels=labels1, autopct='%1.1f%%', startangle=90)
    ax.set(aspect="equal", title='Patients who had a fever')
    plt.savefig("feverTING1.png", bbox_inches = "tight", dpi=300)
    plt.show()

    # Create the second donut chart
    fig, ax = plt.subplots()
    ax.pie(data2, labels=labels2, autopct='%1.1f%%', startangle=90)
    ax.set(aspect="equal", title='Patients who did not have a fever')
    plt.savefig("feverTING2.png", bbox_inches = "tight", dpi=300)
    plt.show()


def blood_culture_data():
    con = sqlite3.connect("joey_data.db")
    cur = con.cursor()
    find_blood = cur.execute('SELECT COUNT("Blood culture results") FROM joey_data WHERE "Included or Excluded" = "Included" AND "Blood culture results" LIKE "%positive%"  ')
    found_blood  = find_blood.fetchall()
    print(found_blood)

    #51 patients with negative blood culture did not change protocol, 16 did
    #7 patients with positive blood culture did not change protocol, 9 did


def blood_culture_graph():


    
    # Data for the first donut chart
    data1 = [9, 7]
    labels1 = ['Changed Protocol', 'Did not change Protocol',]
# Data for the second donut chart
    data2 = [16, 51,]
    labels2 = ['Changed Protocol', 'Did not change Protocol', ]

# Create the first donut chart
    fig, ax = plt.subplots()
    ax.pie(data1, labels=labels1, autopct='%1.1f%%', startangle=90)
    ax.set(aspect="equal", title='Patients with Positive Blood Culture')
    plt.savefig("blood_culture_1.png", bbox_inches = "tight", dpi=300)
    plt.show()

    # Create the second donut chart
    fig, ax = plt.subplots()
    ax.pie(data2, labels=labels2, autopct='%1.1f%%', startangle=90)
    ax.set(aspect="equal", title='Patients with Negative Blood culture')
    plt.savefig("blood_culture_2.png", bbox_inches = "tight", dpi=300)
    plt.show()


def imuno_comp_data():
    con = sqlite3.connect("joey_data.db")
    cur = con.cursor()
    find_imo = cur.execute('SELECT COUNT("Immunocompromised?") FROM joey_data WHERE "Included or Excluded" = "Included" AND "Immunocompromised?" LIKE "%No%" AND "Antibiotics influenced by biopsy?" LIKE "%changed%" ')
    found_imo = find_imo.fetchall()
    print(found_imo)

    #23 patients who are Immunocompromised did not change course, 6 changed
    #41 patients who are not Immunocompromised did not change course, 20 did





def imuno_comp_graph():
     
    data1 = [6, 23]
    labels1 = ['Changed Protocol', 'Did not change Protocol',]
# Data for the second donut chart
    data2 = [20, 41,]
    labels2 = ['Changed Protocol', 'Did not change Protocol', ]

# Create the first donut chart
    fig, ax = plt.subplots()
    ax.pie(data1, labels=labels1, autopct='%1.1f%%', startangle=90)
    ax.set(aspect="equal", title='Patients who are immunocompromised ')
    plt.savefig("imuno_1.png", bbox_inches = "tight", dpi=300)
    plt.show()

    # Create the second donut chart
    fig, ax = plt.subplots()
    ax.pie(data2, labels=labels2, autopct='%1.1f%%', startangle=90)
    ax.set(aspect="equal", title='Patients who are NOT immunocompromised')
    plt.savefig("imuno_2.png", bbox_inches = "tight", dpi=300)
    plt.show()



def smoking_data():
    df  = pd.read_csv("Copy of spine biopsy data.csv", encoding='latin-1')
    colList = df["Smoking"].value_counts()
    #colList.to_excel("smokingDATA.xlsx")

    drinking = df["Malignancy"].value_counts()
   # drinking.to_excel("Malignancy.xlsx")
    out = df.groupby('Malignancy')['Antibiotics influenced by biopsy?'].value_counts()
    out.to_excel("learning.xlsx")
    print(out)


smoking_data()