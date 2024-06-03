from PySide2.QtWidgets import (QApplication, QMainWindow, QAction, QToolBar, QLabel, 
                               QComboBox, QVBoxLayout, QHBoxLayout, QWidget, QGroupBox, 
                               QLineEdit, QGridLayout, QScrollArea, QPushButton, QDialog, 
                               QTabWidget, QFormLayout, QSizePolicy, QListView, QCheckBox, QRadioButton)
from PySide2.QtGui import QIcon, QPixmap
from PySide2.QtCore import Qt
import sys
import pymxs
import os
import json

sys.path.append(r'C:\Users\nghia.tran\Documents\Sandbox')

from ReadOS import *

def get_max_window():
    return pymxs.runtime.windows.getMAXHWND()

class ProjectMakerWindow(QDialog):
    def __init__(self, parent1=None):
        super(ProjectMakerWindow, self).__init__(parent1)
        self.setWindowTitle("Project Maker")
        self.setFixedSize(500, 600)
        
        main_layout = QVBoxLayout()
        self.setLayout(main_layout)
        
        # Create the group box
        groupbox = QGroupBox("Projects:")
        groupbox_layout = QHBoxLayout()
        groupbox.setLayout(groupbox_layout)
        
        # Create the combo box and buttons
        combo_box = QComboBox()
        combo_box.addItems(["Project 1", "Project 2", "Project 3"])
        combo_box.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        combo_box.setMaximumWidth(int(self.width() * 0.6))
        
        button1 = QPushButton("New Project")
        button2 = QPushButton("Delete Project")
        
        # Add the combo box and buttons to the group box layout
        groupbox_layout.addWidget(combo_box)
        groupbox_layout.addWidget(button1)
        groupbox_layout.addWidget(button2)
        
        # Add the group box to the main layout
        main_layout.addWidget(groupbox)
        
        # Create the tab widget
        tab_widget = QTabWidget()
        
        # Create tabs
        tab1 = QWidget()
        tab2 = QWidget()
        
        tab_widget.addTab(tab1, "Shot/Sequences")
        tab_widget.addTab(tab2, "Assets")
        
        # Create group box for sequences
        groupbox_sequences = QGroupBox("Sequences:")
        groupbox_sequences_layout = QVBoxLayout()
        groupbox_sequences.setLayout(groupbox_sequences_layout)
        
        sequencesadd_layout = QHBoxLayout()
        sequences_nameedit = QLineEdit()
        sequences_addbutton = QPushButton("add")
        sequencesadd_layout.addWidget(sequences_nameedit)
        sequencesadd_layout.addWidget(sequences_addbutton)

        sequences_listview = QListView()

        groupbox_sequences_layout.addLayout(sequencesadd_layout)
        groupbox_sequences_layout.addWidget(sequences_listview)

        # Create group box for shots
        groupbox_shots = QGroupBox("Shots:")
        groupbox_shots_layout = QVBoxLayout()
        groupbox_shots.setLayout(groupbox_shots_layout)

        shotadd_layout = QHBoxLayout()
        shotadd_checkBox = QCheckBox("auto")
        shotadd_numberedit = QLineEdit()
        Shotadd_addbutton = QPushButton("add")
        shotadd_layout.addWidget(shotadd_checkBox)
        shotadd_layout.addWidget(shotadd_numberedit)
        shotadd_layout.addWidget(Shotadd_addbutton)

        shotadd_listview = QListView()

        groupbox_shots_layout.addLayout(shotadd_layout)
        groupbox_shots_layout.addWidget(shotadd_listview)

        # Create group box for New Asset Options
        groupbox_newassetopt = QGroupBox("New Asset Option")
        groupbox_newassetopt_layout = QVBoxLayout()
        groupbox_newassetopt.setLayout(groupbox_newassetopt_layout)

        assetmod_lineedit = QLineEdit()
        assetmod_lineedit_label = QLabel("Name:")
        assetmod_lineedit_layout = QVBoxLayout()
        assetmod_lineedit_layout.addWidget(assetmod_lineedit_label)
        assetmod_lineedit_layout.addWidget(assetmod_lineedit)

        assetmod_combobox = QComboBox()
        assetmod_combobox.addItems(["bld","prp","env"])
        assetmod_combobox_label = QLabel("Type:")
        assetmod_combobox_layout = QVBoxLayout()
        assetmod_combobox_layout.addWidget(assetmod_combobox_label)
        assetmod_combobox_layout.addWidget(assetmod_combobox)

        assetmod_layout = QHBoxLayout()
        assetmod_layout.addLayout(assetmod_lineedit_layout)
        assetmod_layout.addLayout(assetmod_combobox_layout)

        assetadd_addbutton = QPushButton("Add New Asset")

        groupbox_newassetopt_layout.addLayout(assetmod_layout)
        groupbox_newassetopt_layout.addWidget(assetadd_addbutton)

        # Create label existing assets
        label_existingasset = QLabel("Existing Assets")
        
        # Create listview existing assets
        existingasset_listview = QListView()

        # Set layouts for tabs (you can customize these as needed)
        tab1_layout = QHBoxLayout()
        tab1.setLayout(tab1_layout)
        tab1_layout.addWidget(groupbox_sequences)
        tab1_layout.addWidget(groupbox_shots)

        tab2_layout = QVBoxLayout()
        tab2.setLayout(tab2_layout)
        tab2_layout.addWidget(groupbox_newassetopt)
        tab2_layout.addWidget(label_existingasset)
        tab2_layout.addWidget(existingasset_listview)
        
        # Add the tab widget to the main layout
        main_layout.addWidget(tab_widget)

class CreateNewWorkfileWindow(QDialog):
    def __init__(self, parent2=None):
        super(CreateNewWorkfileWindow, self).__init__(parent2)
        self.setWindowTitle("Create New Workfile")
        self.setFixedSize(500, 200)

        main_layout = QVBoxLayout()
        self.setLayout(main_layout)

        #Context Area from here
        groupbox_context = QGroupBox("Context:")
        groupbox_context_layout = QHBoxLayout()
        
        
        contextA_label = QLabel("Project:")
        contextA_label_result = QLabel("Coconut")
        contextA_layout = QHBoxLayout()
        contextA_layout.addWidget(contextA_label)
        contextA_layout.addWidget(contextA_label_result)

        contextB_label = QLabel("Squences:")
        contextB_label_result = QLabel("Coconut")
        contextB_layout = QHBoxLayout()
        contextB_layout.addWidget(contextB_label)
        contextB_layout.addWidget(contextB_label_result)

        contextC_label = QLabel("Shot:")
        contextC_label_result = QLabel("Coconut")
        contextC_layout = QHBoxLayout()
        contextC_layout.addWidget(contextC_label)
        contextC_layout.addWidget(contextC_label_result)

        groupbox_context_layout.addLayout(contextA_layout)
        groupbox_context_layout.addLayout(contextB_layout)
        groupbox_context_layout.addLayout(contextC_layout)

        groupbox_context.setLayout(groupbox_context_layout)

        bold_style = "font-weight: bold;"
        contextA_label.setStyleSheet(bold_style)
        contextB_label.setStyleSheet(bold_style)
        contextC_label.setStyleSheet(bold_style)

        left_align_style = "text-align: left;"
        #contextA_label_result.setAlignment(Qt.AlignLeft)
        #contextB_label_result.setAlignment(Qt.AlignLeft)
        #contextC_label_result.setAlignment(Qt.AlignLeft)

        #Options Area from here
        groupbox_options = QGroupBox("Options:")
        groupbox_options_layout = QVBoxLayout()

        groupbox_fileusefile = QGroupBox("File Use File")
        groupbox_fileusefile_layout = QHBoxLayout()
        RadioButton_profilestartupfile = QRadioButton("Profile Startup File")
        RadioButton_currentfile = QRadioButton("Current File")
        groupbox_fileusefile_layout.addWidget(RadioButton_profilestartupfile)
        groupbox_fileusefile_layout.addWidget(RadioButton_currentfile)
        groupbox_fileusefile.setLayout(groupbox_fileusefile_layout)


        groupbox_filenameandtype = QGroupBox("FileName and Type")
        groupbox_filenameandtype_layout = QHBoxLayout()
        Lineedit_filenameandtype = QLineEdit()
        Combobox_Filenameandtype = QComboBox()
        Combobox_Filenameandtype.addItems(["ani","cam","comp"])
        groupbox_filenameandtype_layout.addWidget(Lineedit_filenameandtype)
        groupbox_filenameandtype_layout.addWidget(Combobox_Filenameandtype)
        groupbox_filenameandtype.setLayout(groupbox_filenameandtype_layout)

        groupbox_options_layout.addWidget(groupbox_fileusefile)
        groupbox_options_layout.addWidget(groupbox_filenameandtype)

        groupbox_options.setLayout(groupbox_options_layout)

        #Button Area from here
        groupbox_createbutton = QPushButton("Create Resources")

        main_layout.addWidget(groupbox_context)
        main_layout.addWidget(groupbox_options)
        main_layout.addWidget(groupbox_createbutton)

class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        
        # Set the window size
        self.setFixedSize(1200, 600)
        
        # Set the window title
        self.setWindowTitle("Teddy the Manager by Nghia.Tran")
        
        # Create the main widget and layout
        main_widget = QWidget()
        main_layout = QVBoxLayout()
        main_widget.setLayout(main_layout)
        self.setCentralWidget(main_widget)
        
        # Create the toolbar
        self.create_toolbar()
        
        # Create the user selector
        self.create_user_selector(main_layout)
        
        # Create the context groupbox
        self.create_context_groupbox(main_layout)
        
        # Create the workarea groupbox
        self.create_workarea_groupbox(main_layout)
    
    def create_toolbar(self):
        # Initialize the toolbar
        toolbar = QToolBar("Main Toolbar")
        
        # Lock the toolbar to prevent moving and floating
        toolbar.setMovable(False)
        toolbar.setFloatable(False)
        
        self.addToolBar(toolbar)
        
        # Create actions for the toolbar
        option1_action = QAction("Run Project Manager", self)
        option2_action = QAction("createNew", self)
        option3_action = QAction("checkOut", self)
        option4_action = QAction("Save Over Version", self)
        
        # Add actions to the toolbar
        toolbar.addAction(option1_action)
        toolbar.addAction(option2_action)
        toolbar.addAction(option3_action)
        toolbar.addAction(option4_action)
        
        # Connect actions to methods
        option1_action.triggered.connect(self.option1_triggered)
        option2_action.triggered.connect(self.option2_triggered)
        option3_action.triggered.connect(self.option3_triggered)
        option4_action.triggered.connect(self.option4_triggered)
    
    def create_user_selector(self, layout):
        # Create a horizontal layout for the user selector
        user_layout = QHBoxLayout()
        
        # Create the label
        user_label = QLabel("Current user:")
        user_layout.addWidget(user_label)
        
        # Create the user combo box
        self.user_combo_box = QComboBox()
        self.load_user_names_into_combobox()
        user_layout.addWidget(self.user_combo_box)
        
        # Add the user selector layout to the main layout
        layout.addLayout(user_layout)
    
    def load_user_names_into_combobox(self):
        user_folders = load_folders(USER_DATA_DIRECTORY)
        self.user_combo_box.clear()
        for user_folder in user_folders:
            self.user_combo_box.addItem(user_folder)

    def create_context_groupbox(self, layout):
        # Create the group box
        groupbox = QGroupBox("Context")
        groupbox_layout = QVBoxLayout()
        groupbox.setLayout(groupbox_layout)
        
        # Create the search bar layout
        search_layout = QHBoxLayout()
        
        # Create the search icon
        search_icon = QLabel()
        pixmap = QPixmap("C:\\Users\\nghia.tran\\Downloads\\photo_2024-05-29_11-23-33.png")
        search_icon.setPixmap(pixmap)
        search_layout.addWidget(search_icon)
        
        # Create the search bar
        search_bar = QLineEdit()
        search_bar.setPlaceholderText("Search...")
        search_layout.addWidget(search_bar)
        
        # Add the search bar layout to the group box layout
        groupbox_layout.addLayout(search_layout)
        
        # Create the combobox layout
        combobox_layout = QGridLayout()
        
        # Create the combo boxes and their labels
        
        label3 = QLabel("Shot:")
        self.combo_box3 = QComboBox() 
        self.combo_box3.currentIndexChanged.connect(self.on_shot_folder_selected)
        combobox_layout.addWidget(label3, 0, 2)
        combobox_layout.addWidget(self.combo_box3, 1, 2)
        
        label2 = QLabel("Sequences:")
        self.combo_box2 = QComboBox() 
        self.combo_box2.currentIndexChanged.connect(self.on_sequence_folder_selected)
        combobox_layout.addWidget(label2, 0, 1)
        combobox_layout.addWidget(self.combo_box2, 1, 1)
        
        
        label1 = QLabel("Project:")
        self.combo_box1 = QComboBox() 
        self.combo_box1.currentIndexChanged.connect(self.on_project_folder_selected)
        self.load_project_folders_into_combobox()
        combobox_layout.addWidget(label1, 0, 0)
        combobox_layout.addWidget(self.combo_box1, 1, 0)
        
        
        
        
        
        # Add the combobox layout to the group box layout
        groupbox_layout.addLayout(combobox_layout)
        
        # Add the group box to the main layout
        layout.addWidget(groupbox)

    def load_project_folders_into_combobox(self):
        project_folders = load_project_folders(PROJECT_DIRECTORY)
        self.combo_box1.clear()
        self.combo_box1.addItem("")  # Add empty item by default
        for project_folder in project_folders:
            self.combo_box1.addItem(project_folder)
    
    def load_child_folders_into_combobox(self, directory, combobox):
        try:
            child_folders = load_child_folders(directory)
        except WindowsError as e:
            print("Error loading child folders: {}".format(e))
            child_folders = []
        
        combobox.clear()
        if not child_folders:
            combobox.addItem("empty")
        else:
            for child_folder in child_folders:
                combobox.addItem(child_folder)

    def on_project_folder_selected(self, index):
        
        if index == 0:
            self.combo_box2.clear()
            self.combo_box2.addItem("")
            self.combo_box3.clear()
            self.combo_box3.addItem("")
            self.update_context_label()
            return

        selected_folder = self.combo_box1.itemText(index)
        sequences_folder_path = os.path.join(PROJECT_DIRECTORY, selected_folder, "_sequences")
        print("Loading sequences from: {}".format(sequences_folder_path))  # Debug print
        self.load_child_folders_into_combobox(sequences_folder_path, self.combo_box2)
        # Clear combo_box3 when a new project is selected
        self.combo_box3.clear()
        self.combo_box3.addItem("empty")
        self.update_context_label()

    def on_sequence_folder_selected(self, index):
        # Remove the check for index == 0
        selected_folder = self.combo_box2.itemText(index)
        sequence_folder_path = os.path.join(PROJECT_DIRECTORY, self.combo_box1.currentText(), "_sequences", selected_folder)
        print("Loading shots from: {}".format(sequence_folder_path))  # Debug print
        self.load_child_folders_into_combobox(sequence_folder_path, self.combo_box3)
        self.update_context_label()

    def on_shot_folder_selected(self, index):
        self.update_context_label()

    

    def update_context_label(self):
        
        self.footer_label = QLabel()
        context_text = "context({}_{}_{})".format(self.combo_box1.currentText(), self.combo_box2.currentText(), self.combo_box3.currentText())
        print("context({})".format(context_text))
        self.footer_label.setText(context_text)
        

    def create_workarea_groupbox(self, layout):
        # Create the group box
        groupbox = QGroupBox("Workarea")
        groupbox_layout = QVBoxLayout()
        groupbox.setLayout(groupbox_layout)
        
        # Create the header layout
        header_layout = QHBoxLayout()
        
        # Create the column labels
        resources_label = QLabel("Resources")
        version_label = QLabel("Version")
        snapshot_label = QLabel("Snapshot")
        
        header_layout.addWidget(resources_label)
        header_layout.addWidget(version_label)
        header_layout.addWidget(snapshot_label)
        
        groupbox_layout.addLayout(header_layout)
        
        # Create the scroll areas for the columns
        resources_scroll = self.create_scroll_area()
        version_scroll = self.create_scroll_area()
        snapshot_scroll = self.create_scroll_area()
        
        # Create the columns layout
        columns_layout = QHBoxLayout()
        columns_layout.addWidget(resources_scroll)
        columns_layout.addWidget(version_scroll)
        columns_layout.addWidget(snapshot_scroll)
        
        groupbox_layout.addLayout(columns_layout)
        
       
        
        
        
        # Add the footer label to the group box layout
        groupbox_layout.addStretch()
        groupbox_layout.addWidget(self.footer_label, alignment=Qt.AlignBottom | Qt.AlignLeft)
        
        # Add the group box to the main layout
        layout.addWidget(groupbox)
    
    def populateModel(self):
        whitelist = ['mdl_master', 'rig_master', 'lgt_master', 'anim_master']
        directory = '{}\\{}\\{}\\{}'.format(PROJECT_DIRECTORY,self.combo_box1.currentText(), self.combo_box2.currentText(), self.combo_box3.currentText())

        for folder_name in os.listdir(directory):
            folder_path = os.path.join(directory, folder_name)
            if os.path.isdir(folder_path) and folder_name in whitelist:
                max_files = self.find_max_files_in_highest_version(folder_path)
                for max_file in max_files:
                    self.addButton(max_file)

    def find_max_files_in_highest_version(self, folder_path):
            version_folders = [f for f in os.listdir(folder_path) if os.path.isdir(os.path.join(folder_path, f)) and f.startswith('v')]
            if not version_folders:
                return []

            version_folders_sorted = sorted(version_folders, key=lambda f: int(f[1:]), reverse=True)
            for version_folder in version_folders_sorted:
                highest_version_path = os.path.join(folder_path, version_folder)
                max_files = [f for f in os.listdir(highest_version_path) if os.path.isfile(os.path.join(highest_version_path, f)) and f.endswith('.max')]
                if max_files:
                    return [os.path.join(highest_version_path, f) for f in max_files]


    def create_scroll_area(self):
        scroll_area = QScrollArea()
        scroll_area.setWidgetResizable(True)
        
        # Create a container widget
        container = QWidget()
        scroll_layout = QVBoxLayout()
        
        # Example file info boxes
        for i in range(5):  # Create 5 example file info boxes
            file_info_box = self.create_file_info_box(
                "ani_master_v0001", "ANI_MASTER", 
                "05/27/2024 13:11:10 by Nga.beo"
            )
            scroll_layout.addWidget(file_info_box)
        
        container.setLayout(scroll_layout)
        scroll_area.setWidget(container)
        
        return scroll_area
    
    def create_file_info_box(self, version, project_type, timestamp):
        file_info_box = QPushButton()
        file_info_box.setFixedHeight(100)
        file_info_box.setStyleSheet("text-align: left; padding: 5px; background-color: transparent; border: none;")
        file_info_box.clicked.connect(self.file_info_box_clicked)
        
        # Create a layout for the file info box
        box_layout = QHBoxLayout()
        
        # Icon area
        icon_label = QLabel()
        icon_pixmap = QPixmap("C:\\Users\\nghia.tran\\Downloads\\photo_2024-05-29_11-23-33.png")
        icon_label.setPixmap(icon_pixmap)
        icon_label.setFixedSize(64, 64)
        box_layout.addWidget(icon_label)
        
        # Text area
        text_layout = QVBoxLayout()
        
        version_label = QLabel(version)
        project_type_label = QLabel(project_type)
        separator_label = QLabel("------------")
        timestamp_label = QLabel(timestamp)
        
        text_layout.addWidget(version_label)
        text_layout.addWidget(project_type_label)
        text_layout.addWidget(separator_label)
        text_layout.addWidget(timestamp_label)
        
        box_layout.addLayout(text_layout)
        
        file_info_box.setLayout(box_layout)
        
        return file_info_box
    
    def file_info_box_clicked(self):
        print("hello")
    
    def option1_triggered(self):
        self.project_maker_window = ProjectMakerWindow(parent1=QWidget.find(get_max_window()))
        self.project_maker_window.show()
    
    def option2_triggered(self):
        self.create_new_workfile_window = CreateNewWorkfileWindow(parent2=QWidget.find(get_max_window()))
        self.create_new_workfile_window.show()
    
    def option3_triggered(self):
        print("Option 3 selected")

    def option4_triggered(self):
        print("Option 4 selected")



if __name__ == "__main__":
    app = QApplication(sys.argv) if not QApplication.instance() else QApplication.instance()
    
    main_window = MainWindow(parent=QWidget.find(get_max_window()))
    main_window.show()
    
    try:
        sys.exit(app.exec_())
    except SystemExit:
        print("Application closed.")
