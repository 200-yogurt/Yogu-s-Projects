import Logic.saveSystem as save
import Logic.menuSystem as menu

def MainLoop():

    save.LoadData()

    menu.MenuLoop()


MainLoop()