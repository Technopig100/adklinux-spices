def GUI(self, Gtk):

    # ========================================
    #               HEADER WINDOW
    # ========================================
    
    hb = Gtk.HeaderBar()
    hb.props.show_close_button = True
    hb.props.title = "Adklinux Spices Application"
    hb.props.subtitle = "Importing the Adklinux keys and repos on Arch Linux"
    self.set_titlebar(hb)

    # ========================================
    #               MAIN WINDOW
    # ========================================

    vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=10)
    vbox.set_size_request(500, 100)
    self.add(vbox)

    # ========================================
    #               GLOBALS
    # ========================================

    hbox1 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)
 
    # ========================================
    #               BUTTONS
    # ========================================

    btn1 = Gtk.Button(label="Get the Adklinux Keys and Packages")
    btn1.set_size_request(550, 100)
    btn1.set_name("label")

    btn1.connect("clicked", self.on_btn1_clicked)

    hbox1.pack_start(btn1, True, True, 0)

    self.lbl_status = Gtk.Label(label="Importing Adklinux keyrings and adding Adklinux repos")

    vbox.pack_start(hbox1, False, False, 0)
    vbox.pack_end(self.lbl_status, False, False, 0)
