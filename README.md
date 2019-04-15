## Summary

This library implements a [k-d-tree](https://en.wikipedia.org/wiki/K-d_tree) as well as the closest neighbor algorithm in N dimensions.

## Requirements

Python 3 is required.

## Distance Formula
This library uses a modification of the [Euclidean Distance Formula](https://en.wikipedia.org/wiki/Euclidean_distance), whereby the square of the Euclidean Distance, rather than the Euclidean Distance itself, is used. This optimization is possible because we're only comparing distances rather than measuring their absolute values. Note that, if using this library to find closest neighbors with 2-dimensional geographical coordinates, the Euclidean Distance Formula will only be accurate for small distances. For large distances, the [Haversine Formula](https://en.wikipedia.org/wiki/Haversine_formula) is needed.

## Example

An example which returns the nearest Chicago CTA Station is implemented, which uses data published on the [Chicago Data Portal](https://data.cityofchicago.org/Transportation/CTA-System-Information-List-of-L-Stops/8pix-ypme). It has its own set of dependencies, which can be installed with:
```bash
pew new <custom_env_name>
pip install -r example/requirements.txt
```
To run:
```bash
example/bin/run
```
## Developer
#### Setup
Create a new virtual environment and install the dependencies:
```bash
pew new <custom_env_name>
pip install -r requirements.txt
```

#### Testing
To test, simply run
```bash
pytest
```

Settings re in setup.cfg.

#### Style
You should regularly run `flake8` from the root of the project. Certain warnings are ignored as defined in setup.cfg.
