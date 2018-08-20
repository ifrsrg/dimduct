; Script generated by the Inno Setup Script Wizard.
; SEE THE DOCUMENTATION FOR DETAILS ON CREATING INNO SETUP SCRIPT FILES!

#define MyAppName "DIMduct"
#define MyAppVersion "2.0"
#define MyAppVersion2 "08-18"
#define MyAppPublisher "IFRS Campus Rio Grande"
#define MyAppURL "http://www.engmec.riogrande.ifrs.edu.br/"
#define MyAppExeName "DIMduct.exe"

; MUDAR ISSO: (local do projeto)                                      <<
#define AppLocal "C:\Users\gabri\OneDrive\Documentos\appready"

[Setup]
; NOTE: The value of AppId uniquely identifies this application.
; Do not use the same AppId value in installers for other applications.
; (To generate a new GUID, click Tools | Generate GUID inside the IDE.)
AppId={{25937AD6-9559-4161-8848-3C1D19E2D42B}
AppName={#MyAppName}
AppVersion={#MyAppVersion}
AppVerName={#MyAppName} {#MyAppVersion2}
AppPublisher={#MyAppPublisher}
AppPublisherURL={#MyAppURL}
AppSupportURL={#MyAppURL}
AppUpdatesURL={#MyAppURL}
DefaultDirName={pf}\{#MyAppName}
DisableProgramGroupPage=yes
OutputBaseFilename=DIMduct-setup
Compression=lzma
SolidCompression=yes
SetupIconFile=imgs\setup_icon.ico
WizardSmallImageFile=imgs\setup_corner.bmp
UninstallDisplayIcon={app}\{#MyAppExeName}

[Languages]
Name: "brazilianportuguese"; MessagesFile: "compiler:Languages\BrazilianPortuguese.isl"

[Tasks]
Name: "desktopicon"; Description: "{cm:CreateDesktopIcon}"; GroupDescription: "{cm:AdditionalIcons}"; Flags: unchecked
Name: "quicklaunchicon"; Description: "{cm:CreateQuickLaunchIcon}"; GroupDescription: "{cm:AdditionalIcons}"; Flags: unchecked; OnlyBelowVersion: 0,6.1

[Files]
Source: "{#AppLocal}\DIMduct.exe"; DestDir: "{app}"; Flags: ignoreversion
Source: "{#AppLocal}\dim\*"; DestDir: "{app}\dim"; Flags: ignoreversion recursesubdirs createallsubdirs
Source: "{#AppLocal}\python\*"; DestDir: "{app}\python"; Flags: ignoreversion recursesubdirs createallsubdirs
Source: "{#AppLocal}\imgs\icon.ico"; DestDir: "{app}\imgs"; Flags: ignoreversion
Source: "{#AppLocal}\DIMduct.py"; DestDir: "{app}"; Flags: ignoreversion
Source: "{#AppLocal}\manual.pdf"; DestDir: "{app}"; Flags: ignoreversion
; NOTE: Don't use "Flags: ignoreversion" on any shared system files

[Icons]
Name: "{commonprograms}\{#MyAppName}"; Filename: "{app}\{#MyAppExeName}"; IconFilename: "{app}\imgs\icon.ico"
Name: "{commondesktop}\{#MyAppName}"; Filename: "{app}\{#MyAppExeName}"; Tasks: desktopicon; Comment: "Dimensionamento de dutos"; IconFilename: "{app}\imgs\icon.ico"
Name: "{userappdata}\Microsoft\Internet Explorer\Quick Launch\{#MyAppName}"; Filename: "{app}\{#MyAppExeName}"; Tasks: quicklaunchicon; IconFilename: "{app}\imgs\icon.ico"

[Run]
Filename: "{app}\{#MyAppExeName}"; Description: "{cm:LaunchProgram,{#StringChange(MyAppName, '&', '&&')}}"; Flags: nowait postinstall skipifsilent
