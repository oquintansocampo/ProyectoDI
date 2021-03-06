from gi.overrides import Gdk
from gi.repository import Gtk
from Ventanas.VentanaCliente import WindowC
from Ventanas.VentanaAdmin import WindowA

__author__ = 'oquintansocampo'


class WindowL(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="Login")
        self.set_border_width(10)
        self.set_default_size(500, 100)

        # LayoutBox
        self.box = Gtk.Box(spacing=6)
        self.box.set_orientation(Gtk.Orientation.VERTICAL)
        self.add(self.box)

        # ListBox
        self.list_box = Gtk.ListBox()
        self.list_box.set_selection_mode(Gtk.SelectionMode.NONE)
        print(self.list_box.get_selection_mode())
        self.box.pack_start(self.list_box, True, True, 0)

        # Row1
        self.row1 = Gtk.ListBoxRow()
        self.hor_box1 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=50)
        self.row1.add(self.hor_box1)
        self.v_box1 = Gtk.Box(Gtk.Orientation.VERTICAL)
        self.hor_box1.pack_start(self.v_box1, True, True, 1)

        # Row2
        self.row2 = Gtk.ListBoxRow()
        self.hor_box2 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=50)
        self.row2.add(self.hor_box2)
        self.v_box2 = Gtk.Box(Gtk.Orientation.VERTICAL)
        self.hor_box2.pack_start(self.v_box2, True, True, 1)

        # Row3
        self.row3 = Gtk.ListBoxRow()
        self.hor_box3 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=50)
        self.row3.add(self.hor_box3)
        self.v_box3 = Gtk.Box(Gtk.Orientation.VERTICAL)
        self.hor_box3.pack_start(self.v_box3, True, True, 1)

        # Row4
        self.row4 = Gtk.ListBoxRow()
        self.hor_box4 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=50)
        self.row4.add(self.hor_box4)
        self.v_box4 = Gtk.Box(Gtk.Orientation.VERTICAL)
        self.hor_box4.pack_start(self.v_box4, True, True, 1)

        # Row4
        self.row5 = Gtk.ListBoxRow()
        self.hor_box5 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=50)
        self.row5.add(self.hor_box5)
        self.v_box5 = Gtk.Box(Gtk.Orientation.VERTICAL)
        self.hor_box5.pack_start(self.v_box5, True, True, 1)

        # Labels
        label_title = Gtk.Label("WELCOME")
        label_user = Gtk.Label("*User: ")
        label_pass = Gtk.Label("*Password: ")
        self.label_requerido = Gtk.Label("(*) Campos requeridos")
        self.label_requerido.set_markup("<small>(*) Campos requeridos</small>")

        # TextFields
        self.field_user = Gtk.Entry()
        self.field_pass = Gtk.Entry()
        self.field_pass.set_visibility(False)
        self.field_user.set_can_focus(True)
        self.field_pass.set_can_focus(True)

        # Buttons
        self.log_button = Gtk.Button(label="Entrar")
        self.log_button.connect("clicked", self.confirmarcion)

        self.v_box1.pack_start(label_title, True, True, 1)
        self.v_box2.pack_start(label_user, True, True, 1)
        self.v_box2.pack_start(self.field_user, True, True, 1)
        self.v_box3.pack_start(label_pass, True, True, 1)
        self.v_box3.pack_start(self.field_pass, True, True, 1)
        self.v_box4.pack_start(self.log_button, True, True, 1)
        self.v_box5.pack_start(self.label_requerido, True, True, 1)

        self.list_box.add(self.row1)
        self.list_box.add(self.row2)
        self.list_box.add(self.row3)
        self.list_box.add(self.row4)
        self.list_box.add(self.row5)

    def confirmarcion(self, button):
        """Confirma que la contraseña y el usuario estan guardados"""
        usuarios = {"cliente": "cliente", "admin": "admin"}
        nombre = self.field_user.get_text()
        pass1 = self.field_pass.get_text()
        if (nombre == ""):
            self.label_requerido.override_color(Gtk.StateFlags.NORMAL, Gdk.Color.parse('#ffff00'))
        else:
            pass2 = usuarios[nombre]
            if (pass2 == pass1):
                print("Login succesfull")
                # ConexionBD()
                self.close()
                if (nombre == "cliente"):
                    self.cargarVentanaCli()
                if (nombre == "admin"):
                    self.cargarVentanaAdmin()
            else:
                print("ERROR: Contraseña o nombre de usuario incorrectos")

    def cargarVentanaCli(self):
        """Carga la ventana de Cliente"""
        fiestra = WindowC()
        fiestra.set_position(Gtk.WindowPosition.CENTER)
        fiestra.set_resizable(True)
        fiestra.connect("delete-event", Gtk.main_quit)
        # Mostrar ventana
        fiestra.show_all()
        # fiestra.set_decorated(True)
        # Activar atencion de eventos
        Gtk.main()

    def cargarVentanaAdmin(self):
        """Carga la ventana del Administrador"""
        fiestra = WindowA()
        fiestra.set_position(Gtk.WindowPosition.CENTER)
        fiestra.set_resizable(True)
        fiestra.connect("delete-event", Gtk.main_quit)
        # Mostrar ventana
        fiestra.show_all()
        # fiestra.set_decorated(True)
        # Activar atencion de eventos
        Gtk.main()
