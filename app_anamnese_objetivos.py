import tkinter as tk
from tkinter import messagebox
from fpdf import FPDF

# Perguntas por área
questions = {
    "Finanças": "Quais são seus principais objetivos financeiros?",
    "Saúde e Bem-estar": "Quais metas você tem para sua saúde física e mental?",
    "Relacionamentos": "Que tipo de relacionamentos você deseja cultivar?",
    "Espiritualidade": "Como você pretende desenvolver sua espiritualidade?",
    "Conhecimento": "Que áreas do conhecimento você gostaria de explorar?",
    "Profissional e Carreira": "Quais são suas metas profissionais e de carreira?",
    "Social": "Como você gostaria de se envolver socialmente?",
    "Recreativo (Lazer e Hobbies)": "Quais atividades de lazer e hobbies você gostaria de praticar?"
}

# Função para gerar o PDF
def gerar_pdf(respostas):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    pdf.set_auto_page_break(auto=True, margin=15)

    pdf.set_fill_color(230, 230, 250)
    pdf.cell(0, 10, "Relatório de Objetivos Pessoais", ln=True, align='C', fill=True)
    pdf.ln(10)

    for area, resposta in respostas.items():
        pdf.set_font("Arial", style='B', size=12)
        pdf.cell(0, 10, area, ln=True)
        pdf.set_font("Arial", size=12)
        pdf.multi_cell(0, 10, resposta)
        pdf.ln(5)

    pdf.output("relatorio_objetivos.pdf")
    messagebox.showinfo("PDF Gerado", "Relatório gerado com sucesso como 'relatorio_objetivos.pdf'.")

# Função para coletar respostas
def coletar_respostas():
    respostas = {}
    for area, entry in entries.items():
        resposta = entry.get("1.0", tk.END).strip()
        respostas[area] = resposta
    gerar_pdf(respostas)

# Interface gráfica
root = tk.Tk()
root.title("Anamnese de Objetivos Pessoais")
root.configure(bg="#f0f8ff")

canvas = tk.Canvas(root, bg="#f0f8ff")
scrollbar = tk.Scrollbar(root, orient="vertical", command=canvas.yview)
scroll_frame = tk.Frame(canvas, bg="#f0f8ff")

scroll_frame.bind(
    "<Configure>",
    lambda e: canvas.configure(
        scrollregion=canvas.bbox("all")
    )
)

canvas.create_window((0, 0), window=scroll_frame, anchor="nw")
canvas.configure(yscrollcommand=scrollbar.set)

entries = {}

for area, pergunta in questions.items():
    frame = tk.Frame(scroll_frame, bg="#f0f8ff", pady=5)
    frame.pack(fill="x", padx=10)
    label = tk.Label(frame, text=pergunta, bg="#f0f8ff", anchor="w", font=("Arial", 10, "bold"))
    label.pack(fill="x")
    entry = tk.Text(frame, height=3, wrap="word", font=("Arial", 10))
    entry.pack(fill="x", pady=2)
    entries[area] = entry

btn_gerar = tk.Button(scroll_frame, text="Gerar Relatório em PDF", command=coletar_respostas, bg="#add8e6", font=("Arial", 10, "bold"))
btn_gerar.pack(pady=10)

canvas.pack(side="left", fill="both", expand=True)
scrollbar.pack(side="right", fill="y")

root.mainloop()
