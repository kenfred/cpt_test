from cpt.packager import ConanMultiPackager
builder = ConanMultiPackager(username="kenfred")
builder.add(settings={"arch": "x86"})
builder.run()
