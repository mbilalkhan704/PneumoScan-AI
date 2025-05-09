import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk
from predictors.pneumonia import predict_pneumonia
import math

class PneumoniaApp:
    def __init__(self, root):
        self.root = root
        self.root.title("PneumoScan AI")
        self.root.geometry("900x600")  # Wider window for side-by-side layout
        self.root.configure(bg="#ffffff")
        self.root.resizable(False, False)
        
        # Professional medical color scheme
        self.colors = {
            "primary": "#005b96",
            "secondary": "#e1f5fe",
            "accent": "#0288d1",
            "background": "#ffffff",
            "text": "#212121",
            "success": "#2e7d32",
            "warning": "#f9a825",
            "danger": "#c62828",
            "border": "#e0e0e0"
        }
        
        # Animation control variables
        self.animation_running = False
        
        self.show_title_screen()

    def show_title_screen(self):
        for widget in self.root.winfo_children():
            widget.destroy()

        # Main container with subtle shadow effect
        main_frame = tk.Frame(self.root, bg="#f5f5f5")
        main_frame.pack(fill="both", expand=True, padx=20, pady=20)

        # White content area
        content_frame = tk.Frame(main_frame, bg=self.colors["background"], 
                               highlightbackground=self.colors["border"],
                               highlightthickness=1)
        content_frame.place(relx=0.5, rely=0.5, anchor="center", width=700, height=500)

        # Professional logo placeholder
        logo_frame = tk.Frame(content_frame, bg=self.colors["background"])
        logo_frame.pack(pady=40)
        
        # App title with professional typography
        title_label = tk.Label(
            logo_frame, 
            text="PneumoScan AI", 
            font=("Helvetica", 28, "bold"), 
            fg=self.colors["primary"],
            bg=self.colors["background"]
        )
        title_label.pack()
        
        subtitle_label = tk.Label(
            logo_frame,
            text="Medical-Grade Pneumonia Detection System",
            font=("Helvetica", 12),
            fg=self.colors["text"],
            bg=self.colors["background"]
        )
        subtitle_label.pack(pady=10)

        # Professional start button
        start_button = tk.Button(
            content_frame,
            text="BEGIN ANALYSIS", 
            font=("Helvetica", 12, "bold"),
            bg=self.colors["primary"],
            fg="white",
            activebackground=self.colors["accent"],
            activeforeground="white",
            bd=0,
            padx=40,
            pady=12,
            command=self.show_upload_screen,
            relief="flat"
        )
        start_button.pack(pady=40)

        # Footer with institution branding
        footer_frame = tk.Frame(content_frame, bg=self.colors["background"])
        footer_frame.pack(side="bottom", fill="x", pady=20)
        
        footer_label = tk.Label(
            footer_frame,
            text="© 2023 Medical AI Diagnostics | Certified HIPAA Compliant",
            font=("Helvetica", 9),
            fg="#757575",
            bg=self.colors["background"]
        )
        footer_label.pack()

    def show_upload_screen(self):
        for widget in self.root.winfo_children():
            widget.destroy()

        # Main container with consistent styling
        main_frame = tk.Frame(self.root, bg="#f5f5f5")
        main_frame.pack(fill="both", expand=True, padx=20, pady=20)

        # White content area
        content_frame = tk.Frame(main_frame, bg=self.colors["background"], 
                               highlightbackground=self.colors["border"],
                               highlightthickness=1)
        content_frame.place(relx=0.5, rely=0.5, anchor="center", width=850, height=550)

        # Header with back button
        header_frame = tk.Frame(content_frame, bg=self.colors["background"])
        header_frame.pack(fill="x", padx=30, pady=20)
        
        back_button = tk.Button(
            header_frame,
            text="◄ Back",
            font=("Helvetica", 10),
            bg=self.colors["background"],
            fg=self.colors["primary"],
            bd=0,
            command=self.show_title_screen
        )
        back_button.pack(side="left")
        
        title_label = tk.Label(
            header_frame,
            text="Upload Chest Radiograph",
            font=("Helvetica", 16, "bold"),
            fg=self.colors["primary"],
            bg=self.colors["background"]
        )
        title_label.pack(side="left", padx=10)

        # Upload area with dashed border
        upload_frame = tk.Frame(
            content_frame,
            bg=self.colors["secondary"],
            highlightbackground=self.colors["primary"],
            highlightthickness=1,
            highlightcolor=self.colors["primary"]
        )
        upload_frame.pack(fill="both", expand=True, padx=30, pady=10)
        
        self.upload_canvas = tk.Canvas(
            upload_frame,
            bg=self.colors["background"],
            highlightthickness=0
        )
        self.upload_canvas.pack(fill="both", expand=True, padx=2, pady=2)
        
        # Professional upload prompt
        self.upload_prompt = tk.Label(
            self.upload_canvas,
            text="\nSupported Formats: DICOM, JPG, PNG",
            font=("Helvetica", 11),
            fg=self.colors["text"],
            bg=self.colors["background"]
        )
        self.upload_prompt.place(relx=0.5, rely=0.5, anchor="center")
        
        # Professional upload button
        upload_button = tk.Button(
            content_frame,
            text="SELECT IMAGE",
            font=("Helvetica", 11, "bold"),
            bg=self.colors["primary"],
            fg="white",
            activebackground=self.colors["accent"],
            command=self.upload_image,
            padx=30,
            pady=8,
            bd=0
        )
        upload_button.pack(pady=20)

    def upload_image(self):
        file_path = filedialog.askopenfilename(
            filetypes=[("Medical Images", "*.dcm *.jpg *.jpeg *.png")],
            title="Select Chest Radiograph"
        )
        
        if file_path:
            try:
                self.show_loading_animation()
                # Process in background to keep UI responsive
                self.root.after(100, lambda: self.process_image(file_path))
            except Exception as e:
                messagebox.showerror("Processing Error", 
                                   f"Unable to analyze image:\n{str(e)}")

    def show_loading_animation(self):
        """Professional loading animation with progress ring"""
        self.upload_prompt.destroy()
        
        # Loading container
        self.loading_frame = tk.Frame(self.upload_canvas, bg=self.colors["background"])
        self.loading_frame.place(relx=0.5, rely=0.5, anchor="center", width=300, height=200)
        
        # Progress ring canvas
        self.progress_canvas = tk.Canvas(
            self.loading_frame,
            bg=self.colors["background"],
            width=100,
            height=100,
            highlightthickness=0
        )
        self.progress_canvas.pack(pady=10)
        
        # Draw initial progress ring
        self.progress_ring = self.progress_canvas.create_arc(
            10, 10, 90, 90,
            start=0,
            extent=0,
            outline=self.colors["primary"],
            width=5,
            style="arc"
        )
        
        # Loading text
        loading_label = tk.Label(
            self.loading_frame,
            text="Analyzing Radiograph",
            font=("Helvetica", 12),
            fg=self.colors["text"],
            bg=self.colors["background"]
        )
        loading_label.pack()
        
        # Percentage text
        self.percent_label = tk.Label(
            self.loading_frame,
            text="0%",
            font=("Helvetica", 10),
            fg=self.colors["primary"],
            bg=self.colors["background"]
        )
        self.percent_label.pack()
        
        # Start animation
        self.animation_running = True
        self.loading_progress = 0
        self.animate_progress_ring()

    def animate_progress_ring(self):
        """Animate the progress ring"""
        if not self.animation_running:
            return
            
        if self.loading_progress < 100:
            self.loading_progress += 2
            extent = (self.loading_progress / 100) * 360
            self.progress_canvas.itemconfig(self.progress_ring, extent=extent)
            self.percent_label.config(text=f"{self.loading_progress}%")
            self.root.after(30, self.animate_progress_ring)
        else:
            self.animation_running = False

    def process_image(self, file_path):
        """Process the image and show results"""
        try:
            # Stop any running animation
            self.animation_running = False
            
            # Get prediction
            label, prob = predict_pneumonia(file_path)
            
            # Display results in side-by-side layout
            self.show_results(file_path, label, prob)
            
        except Exception as e:
            messagebox.showerror("Analysis Error", 
                               f"Failed to complete diagnosis:\n{str(e)}")
            self.reset_upload_screen()

    def show_results(self, file_path, label, probability):
        """Display results in side-by-side layout"""
        # Clear the upload screen
        for widget in self.root.winfo_children():
            widget.destroy()

        # Main container
        main_frame = tk.Frame(self.root, bg="#f5f5f5")
        main_frame.pack(fill="both", expand=True, padx=20, pady=20)

        # White content area
        content_frame = tk.Frame(main_frame, bg=self.colors["background"], 
                               highlightbackground=self.colors["border"],
                               highlightthickness=1)
        content_frame.pack(fill="both", expand=True, padx=20, pady=20)

        # Header with back button
        header_frame = tk.Frame(content_frame, bg=self.colors["background"])
        header_frame.pack(fill="x", pady=(0, 20))
        
        back_button = tk.Button(
            header_frame,
            text="◄ Back to Upload",
            font=("Helvetica", 10),
            bg=self.colors["background"],
            fg=self.colors["primary"],
            bd=0,
            command=self.show_upload_screen
        )
        back_button.pack(side="left")

        # Results container - side by side layout
        results_container = tk.Frame(content_frame, bg=self.colors["background"])
        results_container.pack(fill="both", expand=True)

        # Left panel - Image display
        image_frame = tk.Frame(results_container, bg=self.colors["background"])
        image_frame.pack(side="left", fill="both", expand=True, padx=(0, 20))

        # Load and display image
        img = Image.open(file_path)
        img.thumbnail((400, 400))
        photo = ImageTk.PhotoImage(img)
        
        image_canvas = tk.Canvas(
            image_frame,
            bg=self.colors["background"],
            highlightthickness=0
        )
        image_canvas.pack(fill="both", expand=True, pady=10)
        
        image_canvas.create_image(
            image_canvas.winfo_width()//2,
            image_canvas.winfo_height()//2,
            image=photo
        )
        image_canvas.image = photo  # Keep reference

        # Right panel - Analysis results
        results_frame = tk.Frame(results_container, bg=self.colors["background"])
        results_frame.pack(side="right", fill="both", expand=True)

        # Determine result type
        if "pneumonia" in label.lower():
            color = self.colors["danger"]
            icon = "⚠️ CRITICAL FINDING"
            recommendation = "Recommend immediate clinical correlation"
        else:
            color = self.colors["success"]
            icon = "✅ NORMAL FINDING"
            recommendation = "No immediate intervention required"

        # Result header
        result_header = tk.Frame(results_frame, bg=self.colors["background"])
        result_header.pack(fill="x", pady=(0, 20))
        
        result_icon = tk.Label(
            result_header,
            text=icon,
            font=("Helvetica", 14, "bold"),
            fg=color,
            bg=self.colors["background"]
        )
        result_icon.pack(side="left")

        # Confidence meter
        confidence_frame = tk.Frame(results_frame, bg=self.colors["background"])
        confidence_frame.pack(fill="x", pady=(0, 20))
        
        confidence_label = tk.Label(
            confidence_frame,
            text="Diagnostic Confidence:",
            font=("Helvetica", 12),
            fg=self.colors["text"],
            bg=self.colors["background"]
        )
        confidence_label.pack(anchor="w")

        # Professional progress bar
        progress_container = tk.Frame(confidence_frame, bg="#e0e0e0", height=20, width=300)
        progress_container.pack(fill="x", pady=5)
        progress_container.pack_propagate(False)
        
        progress_bar = tk.Frame(progress_container, bg=color, width=0)
        progress_bar.pack(side="left", fill="y")

        # Percentage label
        percent_label = tk.Label(
            confidence_frame,
            text=f"{probability*100:.1f}%",
            font=("Helvetica", 12, "bold"),
            fg=color,
            bg=self.colors["background"]
        )
        percent_label.pack(anchor="w")

        # Animate progress bar
        def animate_progress(current):
            target_width = int(300 * probability)
            if current < target_width:
                progress_bar.config(width=current)
                percent_label.config(text=f"{min(100, (current/300)*100):.1f}%")
                self.root.after(10, lambda: animate_progress(current + 5))
        
        animate_progress(0)

        # Clinical recommendation
        recommendation_frame = tk.Frame(results_frame, bg=self.colors["background"])
        recommendation_frame.pack(fill="x", pady=(20, 0))
        
        recommendation_label = tk.Label(
            recommendation_frame,
            text="CLINICAL RECOMMENDATION:",
            font=("Helvetica", 10, "bold"),
            fg="#616161",
            bg=self.colors["background"]
        )
        recommendation_label.pack(anchor="w")
        
        recommendation_text = tk.Label(
            recommendation_frame,
            text=recommendation,
            font=("Helvetica", 11),
            fg=self.colors["text"],
            bg=self.colors["background"],
            wraplength=350,
            justify="left"
        )
        recommendation_text.pack(anchor="w", pady=(5, 0))

        # Action buttons
        button_frame = tk.Frame(results_frame, bg=self.colors["background"])
        button_frame.pack(fill="x", pady=(30, 0))
        
        save_button = tk.Button(
            button_frame,
            text="SAVE REPORT",
            font=("Helvetica", 11),
            bg="#e0e0e0",
            fg=self.colors["text"],
            padx=25,
            pady=8
        )
        save_button.pack(side="left", padx=5)
        
        new_analysis_button = tk.Button(
            button_frame,
            text="NEW ANALYSIS",
            font=("Helvetica", 11, "bold"),
            bg=self.colors["primary"],
            fg="white",
            command=self.show_upload_screen,
            padx=25,
            pady=8
        )
        new_analysis_button.pack(side="right")

    def reset_upload_screen(self):
        """Reset the upload screen for a new analysis"""
        self.animation_running = False
        self.show_upload_screen()

if __name__ == "__main__":
    root = tk.Tk()
    
    # Center the window on screen
    window_width = 900
    window_height = 600
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    x = (screen_width // 2) - (window_width // 2)
    y = (screen_height // 2) - (window_height // 2)
    root.geometry(f"{window_width}x{window_height}+{x}+{y}")
    
    app = PneumoniaApp(root)
    root.mainloop()