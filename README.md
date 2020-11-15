# eventlogger

The `eventlogger` program allows the recording of self issued events, where the relation between the time-stamp and the event is crucial. The `eventlogger` can be used for the reverse-engineering of an event-driven system, where events trigger certain actions.

## Output Format

| DateTime          | Text                                 |
| ----------------- | ------------------------------------ |
| 11/15/20 14:27:09 | Installed `eventlogger` on my system |

## Requirements

1. Python **3.8** or *above*
2. Python **Poetry**

## Installation

1. ```bash
   git clone https://github.com/tsabelmann/eventlogger
   ```

2. ```bash
   cd eventlogger
   ```

3. ```bash
   poetry install
   ```

4. ```bash
   poetry run eventlogger
   ```

## Acknowledgements

The output files are currently saved into the directory where the `eventlogger` is executed.

