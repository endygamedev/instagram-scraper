import tkinter as tk
from tkinter import filedialog
import pandas as pd
from scraper import Scraper
from warnings import warn


class App(tk.Tk):
    def __init__(self, *args, **kwargs) -> None:
        """
            **Description:** Class that creates the `root` window

            :param args: all `args` options that have `tkinter.Tk`
            :param kwargs: all `kwargs` options that have `tkinter.Tk`
            :returns: Created window
            :rtype: None
        """
        super().__init__(*args, **kwargs)
        self.title("Instagram Scraper")
        self.__gui()
        self.mainloop()

    def event_btn_start(self) -> None:
        """
            **Description:** Button event `btn_start`, launches the scraper

            :returns: Button event
            :rtype: None
        """
        # Get necessary data from fields
        username = self.__entry_username.get()
        password = self.__entry_password.get()
        profile = self.__entry_profile.get()
        post = self.__entry_post.get()

        # Launch the scraper
        scraper = Scraper(username, password)
        scraper.authentication()
        followers = scraper.get_follower_list(profile)
        likes = scraper.get_likes_list(post)
        scraper.end()

        # Process the data and save it
        save_path = filedialog.asksaveasfilename(defaultextension=".csv")
        if not save_path:
            warn("Warning: You should have saved the data...")

        mask = [1 if follower in likes else 0 for follower in followers]
        table = {"@, username": followers, "liked post (0/1)": mask}
        pd.DataFrame(table).to_csv(save_path, encoding="utf-8")

    @staticmethod
    def event_btn_clear(field: tk.Entry) -> None:
        """
            **Description:** Button event `btn_clear`, clears the `field`

            :param field: field to clear
            :type field: tkinter.Entry
            :returns: Button event
            :rtype: None
        """
        field.delete(0, "end")

    @staticmethod
    def event_btn_show(button: tk.Button, field: tk.Entry) -> None:
        """
            **Description:** Button event `btn_show`, shows or hides the password

            :param button: `btn_show` which shows or hides the password
            :type button: tkinter.Button
            :param field: password field
            :type field: tkinter.Entry
            :returns: Button event
            :rtype: None
        """
        if field.cget("show") == "•":
            button.config(text="hide")
            field.config(show="")
        else:
            button.config(text="show")
            field.config(show="•")

    def __gui(self) -> None:
        """
            **Description:** Draws graphic elements in the window

            :returns: Graphic elements
            :rtype: None
        """
        # Initializing
        lbl_title = tk.Label(self, text="Instagram Scraper", font=("Courier", 45, "italic"))
        frame_data = tk.Frame(self)
        frame_main = tk.Frame(self)

        # Log in frame
        # Username
        lbl_username = tk.Label(frame_data, text="Your username")
        self.__entry_username = tk.Entry(frame_data, width=25)
        btn_username = tk.Button(frame_data, text="clear")
        btn_username.config(command=lambda entry=self.__entry_username: self.event_btn_clear(entry))

        # Password
        lbl_password = tk.Label(frame_data, text="Your password")
        self.__entry_password = tk.Entry(frame_data, show="•", width=25)
        btn_password = tk.Button(frame_data, text="clear")
        btn_password.config(command=lambda entry=self.__entry_password: self.event_btn_clear(entry))
        btn_show = tk.Button(frame_data, text="show")
        btn_show.config(command=lambda btn=btn_show, entry=self.__entry_password: self.event_btn_show(btn, entry))

        # Profile
        lbl_profile = tk.Label(frame_data, text="Profile name")
        self.__entry_profile = tk.Entry(frame_data, width=25)
        btn_profile = tk.Button(frame_data, text="clear")
        btn_profile.config(command=lambda entry=self.__entry_profile: self.event_btn_clear(entry))

        # Post
        lbl_post = tk.Label(frame_data, text="Post link")
        self.__entry_post = tk.Entry(frame_data, width=50)
        btn_post = tk.Button(frame_data, text="clear")
        btn_post.config(command=lambda entry=self.__entry_post: self.event_clear(entry))

        # Bottom frame
        btn_start = tk.Button(frame_main, text="Start", command=self.event_btn_start)
        btn_exit = tk.Button(frame_main, text="Exit", command=self.destroy)

        # Packing
        lbl_title.pack(pady=20)
        frame_data.pack(pady=5)
        lbl_username.grid(row=0, column=0, pady=5, padx=5)
        self.__entry_username.grid(row=0, column=1, padx=5, sticky=tk.W)
        btn_username.grid(row=0, column=2, padx=5)
        lbl_password.grid(row=1, column=0, pady=5, padx=5)
        self.__entry_password.grid(row=1, column=1, padx=5, sticky=tk.W)
        btn_password.grid(row=1, column=2, padx=5)
        btn_show.grid(row=1, column=3, padx=5)
        lbl_profile.grid(row=2, column=0, pady=5, padx=5)
        self.__entry_profile.grid(row=2, column=1, padx=5, sticky=tk.W)
        btn_profile.grid(row=2, column=2, padx=5)
        lbl_post.grid(row=3, column=0, pady=5, padx=5)
        self.__entry_post.grid(row=3, column=1, padx=5, sticky=tk.W)
        btn_post.grid(row=3, column=2, padx=5)

        frame_main.pack(pady=20, padx=5)
        btn_start.pack(pady=10)
        btn_exit.pack(pady=5)


if __name__ == "__main__":
    App(className="Instagram Scraper")
