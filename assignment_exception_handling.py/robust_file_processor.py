import csv


def process_csv(filepath):
    file = None

    try:
        file = open(filepath, "r")
        reader = csv.reader(file)

        data = list(reader)

        if len(data) <= 1:
            print("No data found.")
            return

        num_cols = len(data[0])
        sums = [0] * num_cols
        count = 0

        for row in data:
            try:
                numbers = [float(x) for x in row]

                for i in range(num_cols):
                    sums[i] += numbers[i]

                count += 1

            except ValueError:
                print("Skipping malformed row:", row)

        averages = [s / count for s in sums]

        print("Column Averages:")
        for i, avg in enumerate(averages, start=1):
            print(f"Column {i}: {avg}")

    except FileNotFoundError:
        print("File not found!")

    except PermissionError:
        print("Permission denied!")

    except csv.Error:
        print("CSV format error!")

    finally:
        if file:
            file.close()
            print("File closed successfully.")


process_csv("data.csv")