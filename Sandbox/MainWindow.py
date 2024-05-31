class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        
        # Set the window size
        self.setFixedSize(800, 600)
        
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
        label = QLabel("Current user:")
        user_layout.addWidget(label)
        
        # Create the combo box
        combo_box = QComboBox()
        combo_box.addItems(["User1", "User2", "User3"])
        user_layout.addWidget(combo_box)
        
        # Add the user selector layout to the main layout
        layout.addLayout(user_layout)
    
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
        label1 = QLabel("Project:")
        self.combo_box1 = QComboBox()
        self.combo_box1.currentIndexChanged.connect(self.on_project_folder_selected)
        self.load_project_folders_into_combobox()
        combobox_layout.addWidget(label1, 0, 0)
        combobox_layout.addWidget(self.combo_box1, 1, 0)
        
        label2 = QLabel("Sequences:")
        self.combo_box2 = QComboBox()
        combobox_layout.addWidget(label2, 0, 1)
        combobox_layout.addWidget(self.combo_box2, 1, 1)
        
        label3 = QLabel("Shot:")
        self.combo_box3 = QComboBox()
        self.combo_box3.addItems(["Option 1", "Option 2", "Option 3"])
        combobox_layout.addWidget(label3, 0, 2)
        combobox_layout.addWidget(self.combo_box3, 1, 2)
        
        # Add the combobox layout to the group box layout
        groupbox_layout.addLayout(combobox_layout)
        
        # Add the group box to the main layout
        layout.addWidget(groupbox)

    def load_project_folders_into_combobox(self):
        project_folders = load_project_folders(PROJECT_DIRECTORY)
        self.combo_box1.clear()
        for project_folder in project_folders:
            self.combo_box1.addItem(project_folder)
    
    def on_project_folder_selected(self, index):
        selected_folder = self.combo_box1.itemText(index)
        project_folder_path = os.path.join(PROJECT_DIRECTORY, selected_folder)
        self.load_child_folders_into_combobox(project_folder_path)
    
    def load_child_folders_into_combobox(self, directory):
        child_folders = load_child_folders(directory)
        self.combo_box2.clear()
        for child_folder in child_folders:
            self.combo_box2.addItem(child_folder)