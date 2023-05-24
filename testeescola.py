import aspose.words as aw

fileNames = [ "Input1.docx", "Input2.docx" ]

output = aw.Document()
# Remova todo o conteúdo do documento de destino antes de anexar.
output.remove_all_children()

for fileName in fileNames:
    input = aw.Document(fileName)
    # Anexe o documento de origem ao final do documento de destino.
    output.append_document(input, aw.ImportFormatMode.KEEP_SOURCE_FORMATTING)

output.save("Output.pdf");
