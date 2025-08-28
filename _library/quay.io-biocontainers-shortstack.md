---
layout: container
name:  "quay.io/biocontainers/shortstack"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/shortstack/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/shortstack/container.yaml"
updated_at: "2025-08-28 12:15:44.883246"
latest: "4.1.2--hdfd78af_0"
container_url: "https://biocontainers.pro/tools/shortstack"
aliases:
 - "ShortStack"
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
 - "3.8.5--hdfd78af_4"
 - "4.0.0--hdfd78af_0"
 - "4.0.2--hdfd78af_0"
 - "4.0.3--hdfd78af_0"
 - "4.0.4--hdfd78af_0"
 - "4.1.0--hdfd78af_0"
 - "4.0.4--hdfd78af_1"
 - "4.1.2--hdfd78af_0"
description: "shpc-registry automated BioContainers addition for shortstack"
config: {"url": "https://biocontainers.pro/tools/shortstack", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for shortstack", "latest": {"4.1.2--hdfd78af_0": "sha256:86ab704a4d3fb3a736c897f8c99a8c14e8c8cebccda6280a5fd53e6edd2c2571"}, "tags": {"3.8.5--hdfd78af_4": "sha256:c6b2a4d4aa50c0f80ffca2029608bddc9c1019b6df2116e8ee279a8735b6e60f", "4.0.0--hdfd78af_0": "sha256:af4c568f7dd6caee70b9dc5f54fd1cea0db0d00e61355b8b5b47ef397d696e50", "4.0.2--hdfd78af_0": "sha256:f1bebc95158f830c8d70a5f588ce2e24c0176851bf2ecdc9a81360029528ecde", "4.0.3--hdfd78af_0": "sha256:7b18b0efe00f072de1fdda3f1bb12324a6f22dcfe462b63beb3990bc14be1564", "4.0.4--hdfd78af_0": "sha256:d9422937692f7d883737258aa3ce506a88dc980d009c9496f4ee685ec3cc230e", "4.1.0--hdfd78af_0": "sha256:8cfa4d9e6fbe9b42e6e718ce9b1c4b18a6fa8cad4c1b02b9115150882549adb9", "4.0.4--hdfd78af_1": "sha256:ff5173096ea55380ab6a6a6236a7c0c79f6f55c86cb03168ffd854e00c12c61e", "4.1.2--hdfd78af_0": "sha256:86ab704a4d3fb3a736c897f8c99a8c14e8c8cebccda6280a5fd53e6edd2c2571"}, "docker": "quay.io/biocontainers/shortstack", "aliases": {"ShortStack": "/usr/local/bin/ShortStack", "RNAdos": "/usr/local/bin/RNAdos", "AnalyseDists": "/usr/local/bin/AnalyseDists", "AnalyseSeqs": "/usr/local/bin/AnalyseSeqs", "RNAlocmin": "/usr/local/bin/RNAlocmin", "RNApvmin": "/usr/local/bin/RNApvmin", "b2ct": "/usr/local/bin/b2ct", "ct2db": "/usr/local/bin/ct2db", "kinwalker": "/usr/local/bin/kinwalker", "popt": "/usr/local/bin/popt", "RNA2Dfold": "/usr/local/bin/RNA2Dfold"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/shortstack.
shpc-registry automated BioContainers addition for shortstack
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/shortstack
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/shortstack:4.1.2--hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/shortstack/4.1.2--hdfd78af_0
$ module help quay.io/biocontainers/shortstack/4.1.2--hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### shortstack-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### shortstack-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### shortstack-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### shortstack-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### shortstack-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### shortstack-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### ShortStack

```bash
$ singularity exec <container> /usr/local/bin/ShortStack
$ podman run --it --rm --entrypoint /usr/local/bin/ShortStack   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ShortStack   -v ${PWD} -w ${PWD} <container> -c " $@"
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