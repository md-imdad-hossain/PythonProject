import sys

import docx
import os
import docx2txt
from shutil import copyfile
import xml.etree.ElementTree as ET


#   SOFT808 Software User Experience
#   model - Model

class Model:

    cdPath=""
    pathSelectedFile = ""
    nameSelectedFile = ""
    extractedCourseCode = ""
    arrayFolders = []


    def __init__(self):
        print "constructor model"

    def chooseFile(self):
        print "chooseFile"

    def refreshFileName(self):
        print "refreshFileName "

    def enableBtnProcess(self):
        self.btnProcess["state"] = "active"

    def readFile(self, pathFile):
        #print "readFile model " + pathFile
        text = docx2txt.process(pathFile)
        self.cdPath = pathFile
        #Course Code
        indexOneCode = text.find("Course Code")
        indexTwoCode = text.find("Course Title")
        courseCodeText = text[indexOneCode:indexTwoCode].split('\n\n')
        self.extractedCourseCode = str(courseCodeText[1])

        #print self.extractedCourseCode

        #Folder structure
        indexOne = text.find('Summative Assessment')
        indexTwo = text.find('Content')
        #splitResult = text[indexOne:indexTwo].split('\n')
        splitResult = text[indexOne:indexTwo].split('\n\n\n')
        #print text[indexOne:indexTwo]
        #for i in splitResult:
            #print "[" + i + "]"

        secondResult = {}

        for x in range(1, len(splitResult)):
            #print "{" + splitResult[x] + "}"
            secondResult[x-1] = splitResult[x].split('\n')
            #print x

        self.arrayFolders = []
        for j in secondResult:
            if secondResult[j][1] is not None:
                print secondResult[j][1]
                #self.arrayFolders.append(str(secondResult[j][1]))
                self.arrayFolders.append((str(secondResult[j][1])).strip())
            else:
                print "empty row"

    #   SOFT808 Software User Experience
    #   method to generate the folders and copy the files
    def createFolders(self, folderName, pathDestination):
        #print " - createFolders model - "
        #  print "The folders should be created in " + str(pathDestination) + " with the name " + str(folderName)
        backslash = "/"
        main_folder = pathDestination + backslash + folderName

        os.mkdir(main_folder)

        stage_1 = ["Assessment", "ClassRoll", "CourseOutline", "CourseResultSummary", "LectureMaterial", "Other Documents", "SpreadSheet"]

        assesment = self.arrayFolders
        print "\n Model_CreateFolders \n"
        print assesment
        courseOutline = ["Drafts", "ModerationForm"]
        lectureMaterial = ["Book", "Week1", "Week2", "Week3", "Week4", "Week5", "Week7", "Week8", "Week9", "Week10", "Week11", "Week12"]

        drafts = "Soft808.docx"

        moderationMaterial = ["ModerationForms", "ThreeSamples"]
        backslash = "/"

        for w in stage_1:
            os.mkdir(main_folder + backslash + w)

        for x1 in assesment:
            os.mkdir(main_folder + backslash + "Assessment" + backslash + x1)
            os.mkdir(main_folder + backslash + "Assessment" + backslash + x1 + backslash + "Drafts")
            os.mkdir(main_folder + backslash + "Assessment" + backslash + x1 + backslash + "ModerationMaterial")
            os.mkdir(main_folder + backslash + "Assessment" + backslash + x1 + backslash + "Submissions")

        for x2 in courseOutline:
            os.mkdir(main_folder + backslash + "CourseOutline" + backslash + x2)

            week6 = "Week6"
        for x3 in lectureMaterial:
            os.mkdir(main_folder + backslash + "LectureMaterial" + backslash + x3)
        os.mkdir(main_folder + backslash + "LectureMaterial" + backslash + week6)

        destinationFolder = self.cdPath.split('/')

        #print "------------------------------"
        #print destinationFolder

        #copyfile(self.cdPath, main_folder + backslash + "CourseOutline" + backslash + "Drafts" + backslash + destinationFolder[len(destinationFolder) - 1])

        configFile_path = os.path.join(os.getcwd(), "config\\config.xml")
        xmldoc = ET.parse(configFile_path)
        rootXml = xmldoc.getroot()

        titleTemplate1 = rootXml[0].find('title').text
        titleTemplate2 = rootXml[1].find('title').text

        template1_path = os.path.join(os.getcwd(), "Templates\\" + titleTemplate1)
        template2_path = os.path.join(os.getcwd(), "Templates\\" + titleTemplate2)

        template1_destination = main_folder + backslash + "CourseOutline" + backslash + "Drafts" + backslash + titleTemplate1
        copyfile(template1_path, template1_destination)

        template2_destination = main_folder + backslash + "CourseOutline" + backslash + "Drafts" + backslash + titleTemplate2
        copyfile(template2_path, main_folder + backslash + "CourseResultSummary" + backslash + titleTemplate2)
        #copyfile(template2_path, )

        #newDoc = docx.Document()
        #newDoc.add_paragraph("Sample Course Outline")
        #newDoc.save(main_folder + backslash + "CourseOutline" + backslash + "Drafts" + backslash + drafts)

        for z in moderationMaterial:
            for y in self.arrayFolders:
                os.mkdir(
                    main_folder + backslash + "Assessment" + backslash + y + backslash + "ModerationMaterial" + backslash + z)

    def getExtractedCourseCode(self):
        return self.extractedCourseCode

