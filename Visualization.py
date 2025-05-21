from manim_imports_ext import *
import pandas as pd

# Load your data
evt = pd.read_csv("/Users/greinaldpappa/Desktop/simulated_data.csv")  # adjust path as needed

class AverageMedicalSpending(Scene):
    def construct(self):
        # Prepare data
        medical = evt.groupby('event_time')['medical'].mean().sort_index()
        x_vals = [t * 2 for t in medical.index]
        y_vals = medical.values.tolist()

        # Set up axes
        axes = Axes(
            x_range=[min(x_vals), max(x_vals), 5],
            y_range=[0, max(y_vals) * 1.1, max(y_vals) / 5],
            x_length=8,
            y_length=5,
            axis_config={"include_tip": False},
        )
        axes.add_coordinate_labels(font_size=24)

        # Line plot
        graph = axes.get_line_graph(
            x_values=x_vals,
            y_values=y_vals,
            line_color=BLUE,
            add_vertex_dots=False,
        )

        # Vertical zero line
        zero_line = DashedLine(
            axes.c2p(0, 0),
            axes.c2p(0, max(y_vals) * 1.1),
            dash_length=0.1,
            color=GREY,
        )

        # Labels & title
        title = Text("Average Medical Spending", font_size=36).to_edge(UP)
        x_label = axes.get_x_axis_label("Years relative to death", direction=DOWN, buff=0.5)
        y_label = axes.get_y_axis_label("$", direction=LEFT, buff=0.5)

        # Animate
        self.play(Write(title))
        self.play(Create(axes), Write(x_label), Write(y_label))
        self.play(Create(graph), Create(zero_line))
        self.wait(2)


class AverageConsumption(Scene):
    def construct(self):
        # Prepare data
        cons = evt.groupby('event_time')['cons'].mean().sort_index()
        x_vals = [t * 2 for t in cons.index]
        y_vals = cons.values.tolist()

        # Set up axes
        axes = Axes(
            x_range=[min(x_vals), max(x_vals), 5],
            y_range=[0, max(y_vals) * 1.1, max(y_vals) / 5],
            x_length=8,
            y_length=5,
            axis_config={"include_tip": False},
        )
        axes.add_coordinate_labels(font_size=24)

        # Line plot
        graph = axes.get_line_graph(
            x_values=x_vals,
            y_values=y_vals,
            line_color=GREEN,
            add_vertex_dots=False,
        )

        # Vertical zero line
        zero_line = DashedLine(
            axes.c2p(0, 0),
            axes.c2p(0, max(y_vals) * 1.1),
            dash_length=0.1,
            color=GREY,
        )

        # Labels & title
        title = Text("Average Consumption", font_size=36).to_edge(UP)
        x_label = axes.get_x_axis_label("Years relative to death", direction=DOWN, buff=0.5)
        y_label = axes.get_y_axis_label("$", direction=LEFT, buff=0.5)

        # Animate
        self.play(Write(title))
        self.play(Create(axes), Write(x_label), Write(y_label))
        self.play(Create(graph), Create(zero_line))
        self.wait(2)
