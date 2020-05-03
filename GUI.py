from tkinter import *

import math
import Color
import Dimension
import Position
import Block
import Board
import Game


class GUI_Game:

    def __init__(self):
        self.__game_ended_ = False
        self.__nb_rows = 10
        self.__nb_cols = 8
        self.init_gui()
        self.init_board()
        self.build_field()
        self.init_score()
        self.init_level()
        self.init_message()
        self.draw_board()
        self.get_root().mainloop()

    def init_gui(self):
        self.__root_ = Tk()
        self.get_root().title("KU Leuven's Swiper")
        Grid.rowconfigure(self.get_root(), 0, weight=1, minsize=800)
        Grid.columnconfigure(self.get_root(), 0, weight=1, minsize=1200)
        self.__grid_ = Frame(self.get_root())
        self.__grid_.grid(row=0, column=0, sticky=N + S + E + W)
        bottom = Frame(self.get_grid(), bg="black")
        bottom.grid(row=self.get_nb_of_rows_in_board(), sticky=N + S + E + W,
                    columnspan=self.get_nb_of_columns_in_board())
        self.__drawn_blocks_ = set()

    def get_root(self):
        return self.__root_

    def get_grid(self):
        return self.__grid_

    def init_board(self):
        self.__board_ = Board.make_board\
            ((self.get_nb_of_rows_in_board(),self.get_nb_of_columns_in_board()))
        Board.fill_bottom_row(self.get_board(), round(self.get_nb_of_columns_in_board() / 4))

    def get_board(self):
        return self.__board_

    def get_nb_of_rows_in_board(self):
        return self.__nb_rows

    def get_grid_row(self, position):
        if Position.get_row(position) == "X":
            return 0
        else:
            return self.get_nb_of_rows_in_board() - (ord(Position.get_row(position)) - ord("a")) - 1

    def get_nb_of_columns_in_board(self):
        return self.__nb_cols

    def init_score(self):
        self.__score_text_ = StringVar()
        score_lbl = Label(self.get_grid(), textvariable=self.__score_text_, font="Helvetica 24 bold", bg="#eee",
                          fg="black")
        col_floor = math.floor(self.get_nb_of_columns_in_board() / 3)
        score_lbl.grid(row=self.get_nb_of_rows_in_board() + 1,
                       column=self.get_nb_of_columns_in_board() - col_floor, sticky=E,
                       columnspan=col_floor)
        self.set_score(0)

    def set_score(self,new_score):
        self.__score_ = new_score
        self.__score_text_.set("Score: " + str(new_score))

    def get_score(self):
        return self.__score_

    def init_level(self):
        self.__level_text_ = StringVar()
        level_lbl = Label(self.get_grid(), font="Helvetica 24 bold", textvariable=self.__level_text_, bg="#eee",
                          fg="black")
        col_floor = math.floor(self.get_nb_of_columns_in_board() / 3)
        level_lbl.grid(row=self.get_nb_of_rows_in_board() + 1, column=0, sticky=W,
                       columnspan=col_floor)
        self.set_level(1)

    def set_level(self, new_level):
        self.__level_ = new_level
        self.__level_text_.set("Level: " + str(new_level))

    def get_level(self):
        return self.__level_

    def init_message(self):
        self.__message_ = StringVar()
        msg = Label(self.get_grid(), textvariable=self.__message_, bg="#ffa3a3", fg="black")
        col_floor = math.floor(self.get_nb_of_columns_in_board() / 3)
        msg.grid(row=self.get_nb_of_rows_in_board() + 1, column=col_floor, sticky=N + S + E + W,
                 columnspan=self.get_nb_of_columns_in_board() - 2 * col_floor)
        self.set_message("Good luck!")

    def set_message(self, new_message):
        self.__message_.set(new_message)

    def build_field(self):
        nb_rows = Dimension.get_nb_of_rows(Board.get_dimension(self.get_board()))
        nb_cols = Dimension.get_nb_of_columns(Board.get_dimension(self.get_board()))
        for r in range(nb_rows):
            Grid.rowconfigure(self.get_grid(), r, weight=1)
            for c in range(nb_cols):
                Grid.columnconfigure(self.get_grid(), c, weight=1)
                col = "gray" if r == 0 else "white"
                btn = Label(self.get_grid(), state="disabled", bg=col,
                            borderwidth=2, relief="groove")
                btn.grid(row=r, column=c, sticky=N + S + E + W)

    def handle_block_selection(self,event, block):
        if not self.__game_ended_:
            self.__mouse_position_x_at_click_ = event.x
            self.__clicked_block_ = block
            self.__orig_leftmost_clicked_block_pos_ =\
                Board.get_leftmost_position_of(self.get_board(), block)
            self.__new_clicked_block_position_ = self.__orig_leftmost_clicked_block_pos_
            self.__nb_events_to_skip_after_move_ = 3
            Board.remove_block_from(self.get_board(), block)

    def handle_block_move(self,event, drawn_block):
        if not self.__game_ended_:
            delta_mouse_position_x = event.x
            # If the block has just moved, some move events may still refer to the
            # previous position. We therefore skip the first move-event after the
            # block has changed position.
            if self.__nb_events_to_skip_after_move_ > 0:
                self.__nb_events_to_skip_after_move_ -= 1
                return
            cell_width = \
                (self.get_grid().winfo_width() / self.get_nb_of_columns_in_board())
            nb_cells_to_move = \
                round((delta_mouse_position_x - self.__mouse_position_x_at_click_) / cell_width)
            if nb_cells_to_move != 0:
                Board.add_block_at(self.get_board(), self.__clicked_block_, self.__new_clicked_block_position_)
                if Board.can_move_over(self.get_board(), self.__clicked_block_, nb_cells_to_move):
                    self.__nb_events_to_skip_after_move_ = 3
                    if nb_cells_to_move < 0:
                        self.__new_clicked_block_position_ = \
                            Position.left(Board.get_dimension(self.get_board()),
                                          self.__new_clicked_block_position_, abs(nb_cells_to_move))
                    else:
                        self.__new_clicked_block_position_ = \
                            Position.right(Board.get_dimension(self.get_board()),
                                           self.__new_clicked_block_position_, nb_cells_to_move)
                    drawn_block.grid(
                        row=self.get_grid_row(self.__new_clicked_block_position_),
                        column=Position.get_column(self.__new_clicked_block_position_) - 1,
                        sticky=N + S + E + W,
                        columnspan=Block.get_length(self.__clicked_block_))
                Board.remove_block_from(self.get_board(), self.__clicked_block_)

    def handle_block_release(self,event):
        if not self.__game_ended_:
            Board.add_block_at(self.get_board(), self.__clicked_block_, self.__new_clicked_block_position_)
            move_performed =\
                self.__orig_leftmost_clicked_block_pos_ != self.__new_clicked_block_position_
            if move_performed:
                new_level, new_score = \
                    Game.stabilize_board(self.get_level(), self.get_score(), self.get_board())
                self.set_score(new_score)
                self.set_level(new_level)
                self.set_message("...")
                self.draw_board()
                if Board.is_empty_row(self.get_board(), "X"):
                    Board.push_all_blocks_up(self.get_board())
                    self.draw_board()
                    max_block_length = max(2, \
                                           round(self.get_nb_of_columns_in_board() / 4) if self.get_level() <= 3 else \
                                               round(self.get_nb_of_columns_in_board() / 3) if self.get_level() <= 6 else
                                               round(self.get_nb_of_columns_in_board() / 2))
                    Board.fill_bottom_row(self.get_board(), max_block_length)
                    self.draw_board()
                    new_level, new_score = \
                        Game.stabilize_board(self.get_level(), self.get_score(), self.get_board())
                    self.set_score(new_score)
                    self.set_level(new_level)
                    self.set_message("Make a move!")
                    # The board may be completely empty at this point, which would make it
                    # impossible for the player to make the next move.
                    if Board.is_empty_row(self.get_board(), "a"):
                        Board.fill_bottom_row(self.get_board(), max_block_length)
                    self.draw_board()
                else:
                    self.set_message("End of game!")
                    self.end_game()

    def draw_board(self):
        global main_field
        for block in self.__drawn_blocks_:
            block.grid_forget()
        set.clear(self.__drawn_blocks_)
        if not self.__game_ended_:
            dimension_board = Board.get_dimension(self.get_board())
            current_pos = ("X", 1)
            while current_pos is not None:
                block_at_position = Board.get_block_at(self.get_board(), current_pos)
                if block_at_position is not None:
                    self.draw_block(current_pos)
                    step = Block.get_length(block_at_position)
                else:
                    step = 1
                next_pos = Position.right(dimension_board, current_pos, step)
                if next_pos is not None:
                    current_pos = next_pos
                else:
                    current_pos = Position.down(dimension_board, (Position.get_row(current_pos), 1), 1)

    def draw_block(self, position):
        """
           Draw the block at the given position on the given board.
           ASSUMPTIONS
           - The given board is a proper board.
           - The given position is a proper position.
           - The given board has a block whose leftmost position is equal to the
             given position.
        """
        block = Board.get_block_at(self.get_board(), position)
        color_name = Color.get_color_name(Block.get_color(block))
        if Block.get_type(block) == Block.ELECTRIFIED:
            filling = "Electrified"
            rel = RAISED
            thickn = 4
        elif Block.get_type(block) == Block.FRAGILE:
            filling = "Fragile"
            thickn = 2
            rel = SUNKEN
        else:
            filling = ""
            rel = GROOVE
            thickn = 2
        drawn_block = Label(self.get_grid(), text=filling, font="Helvetica 16 bold",
                            bg=color_name, fg="black", relief=rel, bd=4, highlightthickness=thickn,
                            highlightcolor="blue")
        drawn_block.grid(row=self.get_grid_row(position), column=Position.get_column(position) - 1,
                         sticky=N + S + E + W,
                         columnspan=Block.get_length(block))
        drawn_block.bind("<Button-1>",
                         lambda e: self.handle_block_selection(e, block))
        drawn_block.bind("<B1-Motion>",
                         lambda e: self.handle_block_move(e, drawn_block))
        drawn_block.bind("<ButtonRelease-1>",
                         lambda e: self.handle_block_release(e))
        set.add(self.__drawn_blocks_, drawn_block)

    def end_game(self):
        self.__game_ended_ = True


if __name__ == '__main__':


    the_game = GUI_Game()




