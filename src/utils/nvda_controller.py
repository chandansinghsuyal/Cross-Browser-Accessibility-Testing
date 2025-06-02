# Placeholder for NVDA automation utilities
# Requires Windows and NVDA installed
# Example usage with pywinauto

try:
    from pywinauto.application import Application
except ImportError:
    Application = None

def start_nvda():
    if Application is None:
        print('pywinauto not installed or not on Windows.')
        return None
    app = Application().start('nvda.exe')
    return app

def stop_nvda(app):
    if app:
        app.kill() 