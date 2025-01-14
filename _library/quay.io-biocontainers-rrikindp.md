---
layout: container
name:  "quay.io/biocontainers/rrikindp"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/rrikindp/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/rrikindp/container.yaml"
updated_at: "2025-01-14 03:12:42.948354"
latest: "0.0.2--py39h9e0f934_1"
container_url: "https://biocontainers.pro/tools/rrikindp"
aliases:
 - "CopomuS.py"
 - "IntaRNA"
 - "IntaRNA1"
 - "IntaRNA2"
 - "IntaRNA3"
 - "IntaRNA_CSV_p-value.R"
 - "IntaRNA_plotRegions.R"
 - "IntaRNAduplex"
 - "IntaRNAens"
 - "IntaRNAexact"
 - "IntaRNAhelix"
 - "IntaRNAsTar"
 - "IntaRNAseed"
 - "RRIkinDP"
 - "RNAmultifold"
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
 - "RNALalifold"
 - "RNAPKplex"
 - "RNAparconv"
 - "RNAplex"
 - "RNAsnoop"
 - "RNAfold"
 - "Kinfold"
 - "RNALfold"
 - "RNAaliduplex"
 - "RNAalifold"
 - "RNAcofold"
 - "RNAdistance"
 - "RNAduplex"
 - "RNAeval"
versions:
 - "0.0.1--py38h820c706_0"
 - "0.0.2--py39h68928f9_0"
 - "0.0.2--py39h9e0f934_1"
description: "singularity registry hpc automated addition for rrikindp"
config: {"url": "https://biocontainers.pro/tools/rrikindp", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for rrikindp", "latest": {"0.0.2--py39h9e0f934_1": "sha256:5f6da0feb270be32fb695c4304ef42fd3817f16cf5992619208afd2aa90b3d90"}, "tags": {"0.0.1--py38h820c706_0": "sha256:3cc6029f8790d0c2ee284f30abfd10a68ba1c72c707b038af90435f41b7f1352", "0.0.2--py39h68928f9_0": "sha256:23a65de161c8d7e7ac92f558a613f3c6b78fccf5aae8e772b678e044627433a4", "0.0.2--py39h9e0f934_1": "sha256:5f6da0feb270be32fb695c4304ef42fd3817f16cf5992619208afd2aa90b3d90"}, "docker": "quay.io/biocontainers/rrikindp", "aliases": {"CopomuS.py": "/usr/local/bin/CopomuS.py", "IntaRNA": "/usr/local/bin/IntaRNA", "IntaRNA1": "/usr/local/bin/IntaRNA1", "IntaRNA2": "/usr/local/bin/IntaRNA2", "IntaRNA3": "/usr/local/bin/IntaRNA3", "IntaRNA_CSV_p-value.R": "/usr/local/bin/IntaRNA_CSV_p-value.R", "IntaRNA_plotRegions.R": "/usr/local/bin/IntaRNA_plotRegions.R", "IntaRNAduplex": "/usr/local/bin/IntaRNAduplex", "IntaRNAens": "/usr/local/bin/IntaRNAens", "IntaRNAexact": "/usr/local/bin/IntaRNAexact", "IntaRNAhelix": "/usr/local/bin/IntaRNAhelix", "IntaRNAsTar": "/usr/local/bin/IntaRNAsTar", "IntaRNAseed": "/usr/local/bin/IntaRNAseed", "RRIkinDP": "/usr/local/bin/RRIkinDP", "RNAmultifold": "/usr/local/bin/RNAmultifold", "RNAdos": "/usr/local/bin/RNAdos", "AnalyseDists": "/usr/local/bin/AnalyseDists", "AnalyseSeqs": "/usr/local/bin/AnalyseSeqs", "RNAlocmin": "/usr/local/bin/RNAlocmin", "RNApvmin": "/usr/local/bin/RNApvmin", "b2ct": "/usr/local/bin/b2ct", "ct2db": "/usr/local/bin/ct2db", "kinwalker": "/usr/local/bin/kinwalker", "popt": "/usr/local/bin/popt", "RNA2Dfold": "/usr/local/bin/RNA2Dfold", "RNALalifold": "/usr/local/bin/RNALalifold", "RNAPKplex": "/usr/local/bin/RNAPKplex", "RNAparconv": "/usr/local/bin/RNAparconv", "RNAplex": "/usr/local/bin/RNAplex", "RNAsnoop": "/usr/local/bin/RNAsnoop", "RNAfold": "/usr/local/bin/RNAfold", "Kinfold": "/usr/local/bin/Kinfold", "RNALfold": "/usr/local/bin/RNALfold", "RNAaliduplex": "/usr/local/bin/RNAaliduplex", "RNAalifold": "/usr/local/bin/RNAalifold", "RNAcofold": "/usr/local/bin/RNAcofold", "RNAdistance": "/usr/local/bin/RNAdistance", "RNAduplex": "/usr/local/bin/RNAduplex", "RNAeval": "/usr/local/bin/RNAeval"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/rrikindp.
singularity registry hpc automated addition for rrikindp
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/rrikindp
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/rrikindp:0.0.2--py39h9e0f934_1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/rrikindp/0.0.2--py39h9e0f934_1
$ module help quay.io/biocontainers/rrikindp/0.0.2--py39h9e0f934_1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### rrikindp-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### rrikindp-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### rrikindp-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### rrikindp-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### rrikindp-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### rrikindp-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### CopomuS.py

```bash
$ singularity exec <container> /usr/local/bin/CopomuS.py
$ podman run --it --rm --entrypoint /usr/local/bin/CopomuS.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/CopomuS.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### IntaRNA

```bash
$ singularity exec <container> /usr/local/bin/IntaRNA
$ podman run --it --rm --entrypoint /usr/local/bin/IntaRNA   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/IntaRNA   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### IntaRNA1

```bash
$ singularity exec <container> /usr/local/bin/IntaRNA1
$ podman run --it --rm --entrypoint /usr/local/bin/IntaRNA1   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/IntaRNA1   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### IntaRNA2

```bash
$ singularity exec <container> /usr/local/bin/IntaRNA2
$ podman run --it --rm --entrypoint /usr/local/bin/IntaRNA2   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/IntaRNA2   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### IntaRNA3

```bash
$ singularity exec <container> /usr/local/bin/IntaRNA3
$ podman run --it --rm --entrypoint /usr/local/bin/IntaRNA3   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/IntaRNA3   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### IntaRNA_CSV_p-value.R

```bash
$ singularity exec <container> /usr/local/bin/IntaRNA_CSV_p-value.R
$ podman run --it --rm --entrypoint /usr/local/bin/IntaRNA_CSV_p-value.R   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/IntaRNA_CSV_p-value.R   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### IntaRNA_plotRegions.R

```bash
$ singularity exec <container> /usr/local/bin/IntaRNA_plotRegions.R
$ podman run --it --rm --entrypoint /usr/local/bin/IntaRNA_plotRegions.R   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/IntaRNA_plotRegions.R   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### IntaRNAduplex

```bash
$ singularity exec <container> /usr/local/bin/IntaRNAduplex
$ podman run --it --rm --entrypoint /usr/local/bin/IntaRNAduplex   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/IntaRNAduplex   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### IntaRNAens

```bash
$ singularity exec <container> /usr/local/bin/IntaRNAens
$ podman run --it --rm --entrypoint /usr/local/bin/IntaRNAens   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/IntaRNAens   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### IntaRNAexact

```bash
$ singularity exec <container> /usr/local/bin/IntaRNAexact
$ podman run --it --rm --entrypoint /usr/local/bin/IntaRNAexact   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/IntaRNAexact   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### IntaRNAhelix

```bash
$ singularity exec <container> /usr/local/bin/IntaRNAhelix
$ podman run --it --rm --entrypoint /usr/local/bin/IntaRNAhelix   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/IntaRNAhelix   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### IntaRNAsTar

```bash
$ singularity exec <container> /usr/local/bin/IntaRNAsTar
$ podman run --it --rm --entrypoint /usr/local/bin/IntaRNAsTar   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/IntaRNAsTar   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### IntaRNAseed

```bash
$ singularity exec <container> /usr/local/bin/IntaRNAseed
$ podman run --it --rm --entrypoint /usr/local/bin/IntaRNAseed   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/IntaRNAseed   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### RRIkinDP

```bash
$ singularity exec <container> /usr/local/bin/RRIkinDP
$ podman run --it --rm --entrypoint /usr/local/bin/RRIkinDP   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/RRIkinDP   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### RNAmultifold

```bash
$ singularity exec <container> /usr/local/bin/RNAmultifold
$ podman run --it --rm --entrypoint /usr/local/bin/RNAmultifold   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/RNAmultifold   -v ${PWD} -w ${PWD} <container> -c " $@"
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


#### RNALalifold

```bash
$ singularity exec <container> /usr/local/bin/RNALalifold
$ podman run --it --rm --entrypoint /usr/local/bin/RNALalifold   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/RNALalifold   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### RNAPKplex

```bash
$ singularity exec <container> /usr/local/bin/RNAPKplex
$ podman run --it --rm --entrypoint /usr/local/bin/RNAPKplex   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/RNAPKplex   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### RNAparconv

```bash
$ singularity exec <container> /usr/local/bin/RNAparconv
$ podman run --it --rm --entrypoint /usr/local/bin/RNAparconv   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/RNAparconv   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### RNAplex

```bash
$ singularity exec <container> /usr/local/bin/RNAplex
$ podman run --it --rm --entrypoint /usr/local/bin/RNAplex   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/RNAplex   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### RNAsnoop

```bash
$ singularity exec <container> /usr/local/bin/RNAsnoop
$ podman run --it --rm --entrypoint /usr/local/bin/RNAsnoop   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/RNAsnoop   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### RNAfold

```bash
$ singularity exec <container> /usr/local/bin/RNAfold
$ podman run --it --rm --entrypoint /usr/local/bin/RNAfold   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/RNAfold   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### Kinfold

```bash
$ singularity exec <container> /usr/local/bin/Kinfold
$ podman run --it --rm --entrypoint /usr/local/bin/Kinfold   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/Kinfold   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### RNALfold

```bash
$ singularity exec <container> /usr/local/bin/RNALfold
$ podman run --it --rm --entrypoint /usr/local/bin/RNALfold   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/RNALfold   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### RNAaliduplex

```bash
$ singularity exec <container> /usr/local/bin/RNAaliduplex
$ podman run --it --rm --entrypoint /usr/local/bin/RNAaliduplex   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/RNAaliduplex   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### RNAalifold

```bash
$ singularity exec <container> /usr/local/bin/RNAalifold
$ podman run --it --rm --entrypoint /usr/local/bin/RNAalifold   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/RNAalifold   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### RNAcofold

```bash
$ singularity exec <container> /usr/local/bin/RNAcofold
$ podman run --it --rm --entrypoint /usr/local/bin/RNAcofold   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/RNAcofold   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### RNAdistance

```bash
$ singularity exec <container> /usr/local/bin/RNAdistance
$ podman run --it --rm --entrypoint /usr/local/bin/RNAdistance   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/RNAdistance   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### RNAduplex

```bash
$ singularity exec <container> /usr/local/bin/RNAduplex
$ podman run --it --rm --entrypoint /usr/local/bin/RNAduplex   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/RNAduplex   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### RNAeval

```bash
$ singularity exec <container> /usr/local/bin/RNAeval
$ podman run --it --rm --entrypoint /usr/local/bin/RNAeval   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/RNAeval   -v ${PWD} -w ${PWD} <container> -c " $@"
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