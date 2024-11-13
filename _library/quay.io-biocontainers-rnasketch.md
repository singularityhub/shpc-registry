---
layout: container
name:  "quay.io/biocontainers/rnasketch"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/rnasketch/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/rnasketch/container.yaml"
updated_at: "2024-11-13 03:23:57.760393"
latest: "1.5--py_2"
container_url: "https://biocontainers.pro/tools/rnasketch"
aliases:
 - "RNAblueprint"
 - "design-cofold.py"
 - "design-energyshift.py"
 - "design-generategraphml.py"
 - "design-ligandswitch.py"
 - "design-multistate.py"
 - "design-printgraphml.py"
 - "design-redprint-multistate.py"
 - "design-thermoswitch.py"
 - "RNAdos"
 - "igraph"
 - "AnalyseDists"
 - "AnalyseSeqs"
 - "RNAlocmin"
 - "RNApvmin"
 - "b2ct"
 - "ct2db"
 - "kinwalker"
 - "popt"
versions:
 - "1.5--py_2"
description: "shpc-registry automated BioContainers addition for rnasketch"
config: {"url": "https://biocontainers.pro/tools/rnasketch", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for rnasketch", "latest": {"1.5--py_2": "sha256:acbcda0c22ad36f353f166b1f0c7ee669613c30e6750b3d1c2937f5a40854ba2"}, "tags": {"1.5--py_2": "sha256:acbcda0c22ad36f353f166b1f0c7ee669613c30e6750b3d1c2937f5a40854ba2"}, "docker": "quay.io/biocontainers/rnasketch", "aliases": {"RNAblueprint": "/usr/local/bin/RNAblueprint", "design-cofold.py": "/usr/local/bin/design-cofold.py", "design-energyshift.py": "/usr/local/bin/design-energyshift.py", "design-generategraphml.py": "/usr/local/bin/design-generategraphml.py", "design-ligandswitch.py": "/usr/local/bin/design-ligandswitch.py", "design-multistate.py": "/usr/local/bin/design-multistate.py", "design-printgraphml.py": "/usr/local/bin/design-printgraphml.py", "design-redprint-multistate.py": "/usr/local/bin/design-redprint-multistate.py", "design-thermoswitch.py": "/usr/local/bin/design-thermoswitch.py", "RNAdos": "/usr/local/bin/RNAdos", "igraph": "/usr/local/bin/igraph", "AnalyseDists": "/usr/local/bin/AnalyseDists", "AnalyseSeqs": "/usr/local/bin/AnalyseSeqs", "RNAlocmin": "/usr/local/bin/RNAlocmin", "RNApvmin": "/usr/local/bin/RNApvmin", "b2ct": "/usr/local/bin/b2ct", "ct2db": "/usr/local/bin/ct2db", "kinwalker": "/usr/local/bin/kinwalker", "popt": "/usr/local/bin/popt"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/rnasketch.
shpc-registry automated BioContainers addition for rnasketch
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/rnasketch
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/rnasketch:1.5--py_2
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/rnasketch/1.5--py_2
$ module help quay.io/biocontainers/rnasketch/1.5--py_2
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### rnasketch-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### rnasketch-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### rnasketch-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### rnasketch-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### rnasketch-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### rnasketch-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### RNAblueprint

```bash
$ singularity exec <container> /usr/local/bin/RNAblueprint
$ podman run --it --rm --entrypoint /usr/local/bin/RNAblueprint   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/RNAblueprint   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### design-cofold.py

```bash
$ singularity exec <container> /usr/local/bin/design-cofold.py
$ podman run --it --rm --entrypoint /usr/local/bin/design-cofold.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/design-cofold.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### design-energyshift.py

```bash
$ singularity exec <container> /usr/local/bin/design-energyshift.py
$ podman run --it --rm --entrypoint /usr/local/bin/design-energyshift.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/design-energyshift.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### design-generategraphml.py

```bash
$ singularity exec <container> /usr/local/bin/design-generategraphml.py
$ podman run --it --rm --entrypoint /usr/local/bin/design-generategraphml.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/design-generategraphml.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### design-ligandswitch.py

```bash
$ singularity exec <container> /usr/local/bin/design-ligandswitch.py
$ podman run --it --rm --entrypoint /usr/local/bin/design-ligandswitch.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/design-ligandswitch.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### design-multistate.py

```bash
$ singularity exec <container> /usr/local/bin/design-multistate.py
$ podman run --it --rm --entrypoint /usr/local/bin/design-multistate.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/design-multistate.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### design-printgraphml.py

```bash
$ singularity exec <container> /usr/local/bin/design-printgraphml.py
$ podman run --it --rm --entrypoint /usr/local/bin/design-printgraphml.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/design-printgraphml.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### design-redprint-multistate.py

```bash
$ singularity exec <container> /usr/local/bin/design-redprint-multistate.py
$ podman run --it --rm --entrypoint /usr/local/bin/design-redprint-multistate.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/design-redprint-multistate.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### design-thermoswitch.py

```bash
$ singularity exec <container> /usr/local/bin/design-thermoswitch.py
$ podman run --it --rm --entrypoint /usr/local/bin/design-thermoswitch.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/design-thermoswitch.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### RNAdos

```bash
$ singularity exec <container> /usr/local/bin/RNAdos
$ podman run --it --rm --entrypoint /usr/local/bin/RNAdos   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/RNAdos   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### igraph

```bash
$ singularity exec <container> /usr/local/bin/igraph
$ podman run --it --rm --entrypoint /usr/local/bin/igraph   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/igraph   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### AnalyseDists

```bash
$ singularity exec <container> /usr/local/bin/AnalyseDists
$ podman run --it --rm --entrypoint /usr/local/bin/AnalyseDists   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/AnalyseDists   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### AnalyseSeqs

```bash
$ singularity exec <container> /usr/local/bin/AnalyseSeqs
$ podman run --it --rm --entrypoint /usr/local/bin/AnalyseSeqs   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/AnalyseSeqs   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### RNAlocmin

```bash
$ singularity exec <container> /usr/local/bin/RNAlocmin
$ podman run --it --rm --entrypoint /usr/local/bin/RNAlocmin   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/RNAlocmin   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### RNApvmin

```bash
$ singularity exec <container> /usr/local/bin/RNApvmin
$ podman run --it --rm --entrypoint /usr/local/bin/RNApvmin   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/RNApvmin   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### b2ct

```bash
$ singularity exec <container> /usr/local/bin/b2ct
$ podman run --it --rm --entrypoint /usr/local/bin/b2ct   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/b2ct   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ct2db

```bash
$ singularity exec <container> /usr/local/bin/ct2db
$ podman run --it --rm --entrypoint /usr/local/bin/ct2db   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ct2db   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### kinwalker

```bash
$ singularity exec <container> /usr/local/bin/kinwalker
$ podman run --it --rm --entrypoint /usr/local/bin/kinwalker   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/kinwalker   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### popt

```bash
$ singularity exec <container> /usr/local/bin/popt
$ podman run --it --rm --entrypoint /usr/local/bin/popt   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/popt   -v ${PWD} -w ${PWD} <container> -c " $@"
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