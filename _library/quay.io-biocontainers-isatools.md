---
layout: container
name:  "quay.io/biocontainers/isatools"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/isatools/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/isatools/container.yaml"
updated_at: "2025-01-08 06:35:45.345452"
latest: "0.14.2--pyhdfd78af_0"
container_url: "https://biocontainers.pro/tools/isatools"
aliases:
 - "isatools"
 - "mzml2isa"
 - "pronto"
 - "createfontdatachunk.py"
 - "enhancer.py"
 - "explode.py"
 - "gifmaker.py"
 - "painter.py"
 - "player.py"
 - "thresholder.py"
 - "viewer.py"
 - "pilconvert.py"
 - "pildriver.py"
versions:
 - "0.9.5--py36_0"
 - "0.12.2--pyhdfd78af_0"
 - "0.11.0--py_0"
 - "0.10.3--py_1"
 - "0.14.2--pyhdfd78af_0"
 - "0.9.5--py35_0"
description: "shpc-registry automated BioContainers addition for isatools"
config: {"url": "https://biocontainers.pro/tools/isatools", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for isatools", "latest": {"0.14.2--pyhdfd78af_0": "sha256:5c2af7b7d8f4f477be96b3f4f172bb8b33907190822c0a54a5c56bae5ac0bad3"}, "tags": {"0.9.5--py36_0": "sha256:3a87a4e0142dbf26fbe73dab20a3616f56e2e4ceec6bac2d3552678884744f54", "0.12.2--pyhdfd78af_0": "sha256:dd669566c8df3bd9d0d6c57ea850b2cb91699bdd7b24eae09c0e6484dab73212", "0.11.0--py_0": "sha256:41bffbd21deb58b59d92c7136953e92fe0864fed0c37fe3703a722aee2a3eb26", "0.10.3--py_1": "sha256:806b5f738a462dcfd4a3d4df3a94fab1491115b70e70bdd1fa1ac237cb0a1ab8", "0.14.2--pyhdfd78af_0": "sha256:5c2af7b7d8f4f477be96b3f4f172bb8b33907190822c0a54a5c56bae5ac0bad3", "0.9.5--py35_0": "sha256:d2211318fc8d9779a6c0fb63a64f92914085232e460a15959c0a3f363bb42806"}, "docker": "quay.io/biocontainers/isatools", "aliases": {"isatools": "/usr/local/bin/isatools", "mzml2isa": "/usr/local/bin/mzml2isa", "pronto": "/usr/local/bin/pronto", "createfontdatachunk.py": "/usr/local/bin/createfontdatachunk.py", "enhancer.py": "/usr/local/bin/enhancer.py", "explode.py": "/usr/local/bin/explode.py", "gifmaker.py": "/usr/local/bin/gifmaker.py", "painter.py": "/usr/local/bin/painter.py", "player.py": "/usr/local/bin/player.py", "thresholder.py": "/usr/local/bin/thresholder.py", "viewer.py": "/usr/local/bin/viewer.py", "pilconvert.py": "/usr/local/bin/pilconvert.py", "pildriver.py": "/usr/local/bin/pildriver.py"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/isatools.
shpc-registry automated BioContainers addition for isatools
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/isatools
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/isatools:0.14.2--pyhdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/isatools/0.14.2--pyhdfd78af_0
$ module help quay.io/biocontainers/isatools/0.14.2--pyhdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### isatools-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### isatools-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### isatools-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### isatools-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### isatools-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### isatools-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### isatools

```bash
$ singularity exec <container> /usr/local/bin/isatools
$ podman run --it --rm --entrypoint /usr/local/bin/isatools   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/isatools   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mzml2isa

```bash
$ singularity exec <container> /usr/local/bin/mzml2isa
$ podman run --it --rm --entrypoint /usr/local/bin/mzml2isa   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mzml2isa   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pronto

```bash
$ singularity exec <container> /usr/local/bin/pronto
$ podman run --it --rm --entrypoint /usr/local/bin/pronto   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pronto   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### createfontdatachunk.py

```bash
$ singularity exec <container> /usr/local/bin/createfontdatachunk.py
$ podman run --it --rm --entrypoint /usr/local/bin/createfontdatachunk.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/createfontdatachunk.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### enhancer.py

```bash
$ singularity exec <container> /usr/local/bin/enhancer.py
$ podman run --it --rm --entrypoint /usr/local/bin/enhancer.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/enhancer.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### explode.py

```bash
$ singularity exec <container> /usr/local/bin/explode.py
$ podman run --it --rm --entrypoint /usr/local/bin/explode.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/explode.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gifmaker.py

```bash
$ singularity exec <container> /usr/local/bin/gifmaker.py
$ podman run --it --rm --entrypoint /usr/local/bin/gifmaker.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gifmaker.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### painter.py

```bash
$ singularity exec <container> /usr/local/bin/painter.py
$ podman run --it --rm --entrypoint /usr/local/bin/painter.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/painter.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### player.py

```bash
$ singularity exec <container> /usr/local/bin/player.py
$ podman run --it --rm --entrypoint /usr/local/bin/player.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/player.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### thresholder.py

```bash
$ singularity exec <container> /usr/local/bin/thresholder.py
$ podman run --it --rm --entrypoint /usr/local/bin/thresholder.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/thresholder.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### viewer.py

```bash
$ singularity exec <container> /usr/local/bin/viewer.py
$ podman run --it --rm --entrypoint /usr/local/bin/viewer.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/viewer.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pilconvert.py

```bash
$ singularity exec <container> /usr/local/bin/pilconvert.py
$ podman run --it --rm --entrypoint /usr/local/bin/pilconvert.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pilconvert.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pildriver.py

```bash
$ singularity exec <container> /usr/local/bin/pildriver.py
$ podman run --it --rm --entrypoint /usr/local/bin/pildriver.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pildriver.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```



In the above, the `<container>` directive will reference an actual container provided
by the module, for the version you have chosen to load. An environment file in the
module folder will also be bound. Note that although a container
might provide custom commands, every container exposes unique exec, shell, run, and
inspect aliases. For anycommands above, you can export:

 - SINGULARITY_OPTS: to define custom options for singularity (e.g., --debug)
 - SINGULARITY_COMMAND_OPTS: to define custom options for the command (e.g., -b)
 - PODMAN_OPTS: to define custom options for podman or docker
 - PODMAN_COMMAND_OPTS: to define custom options for the command

<br>

### Install

You can install shpc locally (for yourself or your user base) as follows:

```bash
$ git clone https://github.com/singularityhub/singularity-hpc
$ cd singularity-hpc
$ pip install -e .
```

Have any questions, or want to request a new module or version? [ask for help!](https://github.com/singularityhub/singularity-hpc/issues)