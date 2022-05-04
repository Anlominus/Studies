import PySimpleGUIQt as s

mylayout = [
    [s.Text("Hello World"), s.Button("OK")],
    [s.Text("Python is cool"), s.Text("Yes")],
    [s.Text("Learn PySimpleGUI")]
]

window = s.Window(title="Hello World", size=(640,480), layout=mylayout)
window.read()
