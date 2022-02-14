def help():
    print("\t--data=filepos")
    print("\t--data=size")
    print("\t--data=name")
    print("")
    print("\t\tAdd the specified key to the list of metadata to print for each")
    print("\t\tentry. By default for each entry Wadder will print all three")
    print("\t\tmetadata, so normally this is not needed. However it can be used")
    print("\t\tto re-add to the list of metadata if it was removed with")
    print("\t\t'--data-only='.")
    print("")
    print("\t--data-only=filepos")
    print("\t--data-only=size")
    print("\t--data-only=name")
    print("")
    print("\t\tClear the list of metadata to print for each entry, and replace")
    print("\t\tit with only the key specified. If more metadata is needed, use")
    print("\t\t'--data=' to add more to the list.")
    print("")
    print("\t--end=N")
    print("")
    print("\t\tSet the last entry to index (inclusive) when using '--list'.")
    print("\t\tDefaults to the last entry in the directory.")
    print("")
    print("\t--entry=N")
    print("")
    print("\t\tPrint all metadata for a single entry in the directory at index")
    print("\t\tN.")
    print("")
    print("\t--find=string")
    print("")
    print("\t\tFind and print the entry for any lumps which have a name")
    print("\t\tstarting with 'string'. Also save each matching lump if the")
    print("\t\t'--save' flag is set.")
    print("")
    print("\t--header-identification")
    print("\t--header-numlumps")
    print("\t--header-infotableofs")
    print("")
    print("\t\tPrint the requested header information.")
    print("")
    print("\t--index=N")
    print("")
    print("\t\tSet the first entry to index when using '--list'. Defaults to")
    print("\t\tthe first entry [0].")
    print("")
    print("\t--indexed")
    print("")
    print("\t\tPrepend each entry listed by printing its index before the")
    print("\t\tmetadata.")
    print("")
    print("\t--length")
    print("")
    print("\t\tPrint the length of the directory.")
    print("")
    print("\t--list")
    print("")
    print("\t\tPrint each entry in the directory starting with '--index=' and")
    print("\t\tending with '--end='. Each entry is printed on a new line with")
    print("\t\ta blank separator between each metadata. If the '--save' flag")
    print("\t\tis set, save each entry listed as a raw lump file.")
    print("")
    print("\t--save")
    print("")
    print("\t\tSave the lump data from each entry listed as a binary file with")
    print("\t\tthe '.lmp' extension.")
    print("")
    print("\t--save=N")
    print("")
    print("\t\tSave the lump data from the entry at index N as a binary file")
    print("\t\twith the '.lmp' extension.")

def usage():
    print("invoked:", sys.argv[0])
    print("usage: python3 wadder.py <parameters> <filename>")
    print("examples:")
    print("  python3 wadder.py freedoom2.wad")
    print("    parse and print the WAD header information for freedoom2.wad")
    print("  python3 wadder.py --index=10 --end=20 --list freedm.wad")
    print("    print the metadata for each entry from 10 to 20 for freedm.wad")
    print("  python3 wadder.py --find=FLOOR --save Valiant.wad")
    print("    find and save every lump in Valiant.wad named FLOOR*")
    print("  python3 wadder.py --save=100 DOOM2.WAD")
    print("    save the 100th lump found in DOOM2.WAD")
    print("for more help: python3 wadder.py --help")
