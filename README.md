Keylogger 

Steps to Modify for Android
For Android devices, you will need to use a tool like Termux to run Python scripts. You can package the keylogger as a .apk file or use cross-compilation techniques to ensure the script can be executed on Android.

Combining Keylogger with Files
Hiding Keyloggers in Files (Steganography & Document Exploits)
You can demonstrate how cyber attackers embed malware in different file formats. The combination typically includes the use of document macros, file format exploits, or steganography (hiding information in images). However, modern operating systems and antivirus software often block these techniques, so you’ll have to explain how they work conceptually.

Embedding Python Script in Files
PDF: Use mPDF to insert malicious JavaScript or embed Python scripts into PDFs.
Word Documents (.docx): Use macros in Word. When the document is opened, the macro can trigger the keylogger.
VBA Macros Example: 
                    Sub AutoOpen()
                         Shell ("C:\path\to\python.exe C:\path\to\keylogger.py")
                    End Sub
                    
Image Files: Use steganography tools like Steghide to hide the Python keylogger script inside .jpg or .png files.
Automatic Execution of Code
Windows: You can use Windows Task Scheduler or Autorun to automatically execute the keylogger when a user opens a file. For instance, a .bat file can be configured to trigger the keylogger.
Android: A packaged .apk file would execute upon installation, which can include code that runs in the background after the app is opened.
