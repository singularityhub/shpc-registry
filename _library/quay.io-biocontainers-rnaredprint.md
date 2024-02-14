---
layout: container
name:  "quay.io/biocontainers/rnaredprint"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/rnaredprint/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/rnaredprint/container.yaml"
updated_at: "2024-02-14 02:30:31.352299"
latest: "0.3pre--py310h4ac6f70_4"
container_url: "https://biocontainers.pro/tools/rnaredprint"
aliases:
 - "RNARedPrint"
 - "RNARedPrintSampler.py"
 - "RNARedPrintStructure.py"
 - "RNAmultifold"
 - "calcprobs.py"
 - "design-energyshift.py"
 - "design-multistate.py"
 - "RNAdos"
 - "AnalyseDists"
 - "AnalyseSeqs"
 - "RNAlocmin"
 - "RNApvmin"
 - "b2ct"
 - "ct2db"
 - "kinwalker"
 - "popt"
 - "RNA2Dfold"
versions:
 - "0.3pre--py39h9f5acd7_3"
 - "0.3pre--py310h4ac6f70_4"
description: "shpc-registry automated BioContainers addition for rnaredprint"
config: {"url": "https://biocontainers.pro/tools/rnaredprint", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for rnaredprint", "latest": {"0.3pre--py310h4ac6f70_4": "sha256:f1887c1726a027a3f99d490e0ea65687453e59ba4b3947a3240b2504a9e1203a"}, "tags": {"0.3pre--py39h9f5acd7_3": "sha256:9978439c4f91c1fcc5f8cf26461eb0bed59aff5191cf062b0f01e55ab76eff3c", "0.3pre--py310h4ac6f70_4": "sha256:f1887c1726a027a3f99d490e0ea65687453e59ba4b3947a3240b2504a9e1203a"}, "docker": "quay.io/biocontainers/rnaredprint", "aliases": {"RNARedPrint": "/usr/local/bin/RNARedPrint", "RNARedPrintSampler.py": "/usr/local/bin/RNARedPrintSampler.py", "RNARedPrintStructure.py": "/usr/local/bin/RNARedPrintStructure.py", "RNAmultifold": "/usr/local/bin/RNAmultifold", "calcprobs.py": "/usr/local/bin/calcprobs.py", "design-energyshift.py": "/usr/local/bin/design-energyshift.py", "design-multistate.py": "/usr/local/bin/design-multistate.py", "RNAdos": "/usr/local/bin/RNAdos", "AnalyseDists": "/usr/local/bin/AnalyseDists", "AnalyseSeqs": "/usr/local/bin/AnalyseSeqs", "RNAlocmin": "/usr/local/bin/RNAlocmin", "RNApvmin": "/usr/local/bin/RNApvmin", "b2ct": "/usr/local/bin/b2ct", "ct2db": "/usr/local/bin/ct2db", "kinwalker": "/usr/local/bin/kinwalker", "popt": "/usr/local/bin/popt", "RNA2Dfold": "/usr/local/bin/RNA2Dfold"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/rnaredprint.
shpc-registry automated BioContainers addition for rnaredprint
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/rnaredprint
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/rnaredprint:0.3pre--py310h4ac6f70_4
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/rnaredprint/0.3pre--py310h4ac6f70_4
$ module help quay.io/biocontainers/rnaredprint/0.3pre--py310h4ac6f70_4
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### rnaredprint-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### rnaredprint-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### rnaredprint-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### rnaredprint-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### rnaredprint-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### rnaredprint-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### RNARedPrint

```bash
$ singularity exec <container> /usr/local/bin/RNARedPrint
$ podman run --it --rm --entrypoint /usr/local/bin/RNARedPrint   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/RNARedPrint   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### RNARedPrintSampler.py

```bash
$ singularity exec <container> /usr/local/bin/RNARedPrintSampler.py
$ podman run --it --rm --entrypoint /usr/local/bin/RNARedPrintSampler.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/RNARedPrintSampler.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### RNARedPrintStructure.py

```bash
$ singularity exec <container> /usr/local/bin/RNARedPrintStructure.py
$ podman run --it --rm --entrypoint /usr/local/bin/RNARedPrintStructure.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/RNARedPrintStructure.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### RNAmultifold

```bash
$ singularity exec <container> /usr/local/bin/RNAmultifold
$ podman run --it --rm --entrypoint /usr/local/bin/RNAmultifold   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/RNAmultifold   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### calcprobs.py

```bash
$ singularity exec <container> /usr/local/bin/calcprobs.py
$ podman run --it --rm --entrypoint /usr/local/bin/calcprobs.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/calcprobs.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### design-energyshift.py

```bash
$ singularity exec <container> /usr/local/bin/design-energyshift.py
$ podman run --it --rm --entrypoint /usr/local/bin/design-energyshift.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/design-energyshift.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### design-multistate.py

```bash
$ singularity exec <container> /usr/local/bin/design-multistate.py
$ podman run --it --rm --entrypoint /usr/local/bin/design-multistate.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/design-multistate.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### RNAdos

```bash
$ singularity exec <container> /usr/local/bin/RNAdos
$ podman run --it --rm --entrypoint /usr/local/bin/RNAdos   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/RNAdos   -v ${PWD} -w ${PWD} <container> -c " $@"
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


#### RNA2Dfold

```bash
$ singularity exec <container> /usr/local/bin/RNA2Dfold
$ podman run --it --rm --entrypoint /usr/local/bin/RNA2Dfold   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/RNA2Dfold   -v ${PWD} -w ${PWD} <container> -c " $@"
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