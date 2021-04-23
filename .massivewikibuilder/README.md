# Massive Wiki Builder

## Build

In `.massivewikibuilder/`:

```
./mwb.py -w .. -o output -t .
```

## Develop

Because static assets have an absolute path, you may want to start a local web server while your developing and testing.  Change to the output directory and run this command:

```
python3 -m http.server
```
