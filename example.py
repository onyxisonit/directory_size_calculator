from file_system import File, Directory

def build_example_filesystem():
    root = Directory("root")

    docs = Directory("docs")
    docs.add_file(File("resume.pdf", 120))
    docs.add_file(File("resume2.pdf", 122))
    docs.add_file(File("coverletter.pdf", 91))
    docs.add_file(File("portfolio.pdf", 192))
    docs.add_file(File("finalreport.docx", 333))

    desktop = Directory("desktop")
    desktop.add_file(File("screenshot_080725.pdf", 91))
    desktop.add_file(File("screenshot_030625.png", 86))

    music = Directory("music")
    music.add_file(File("lo-fi.mp3", 5900))

    images = Directory("images")
    images.add_file(File("lo-fi.gif", 900))
    images.add_file(File("cat.jpeg", 250))
    images.add_file(File("forest.png", 266))

    media = Directory("media")

    media.add_subdirectory(music)
    media.add_subdirectory(images)

    root.add_subdirectory(docs)
    root.add_subdirectory(desktop)
    root.add_subdirectory(media)

    return root





