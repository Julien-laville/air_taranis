# Air Taranis

## Setup

First download the Leap SDK archive and extract it into a ./SDK folder. There is a `get_sdk` that does it for you, just in case:

```bash
./get_sdk
```
should do the trick.

Then, simply source the environment using the setenv script at the root of the project:

```bash
source ./setenv
```

Now you should be able to use the Leap sdk.
```python
import Leap
```
