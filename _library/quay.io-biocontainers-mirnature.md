---
layout: container
name:  "quay.io/biocontainers/mirnature"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/mirnature/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/mirnature/container.yaml"
updated_at: "2024-07-05 03:14:41.477978"
latest: "1.1--pl5321hdfd78af_2"
container_url: "https://biocontainers.pro/tools/mirnature"
aliases:
 - "MIRfix.py"
 - "dialign2-2"
 - "evaluate_conserved_str.py"
 - "miRNAnchor.pl"
 - "miRNAture"
 - "miRNAture.pl"
 - "runMIRfix.sh"
 - "testMIRfix.sh"
 - "rmblastn"
 - "clustalo"
 - "blast_report"
 - "blastdb_convert"
 - "blastdb_path"
 - "bl2seq"
 - "blastall"
 - "blastclust"
 - "blastpgp"
 - "copymat"
versions:
 - "1.0--pl5262r35hdfd78af_5"
 - "1.1--pl5321r41hdfd78af_0"
 - "1.1--pl5321hdfd78af_1"
 - "1.1--pl5321hdfd78af_2"
description: "shpc-registry automated BioContainers addition for mirnature"
config: {"url": "https://biocontainers.pro/tools/mirnature", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for mirnature", "latest": {"1.1--pl5321hdfd78af_2": "sha256:e8f4c1b3e3c72c14bea0c1b91639e3be82bd2e4f087ec7e95dbbeb170a60465b"}, "tags": {"1.0--pl5262r35hdfd78af_5": "sha256:51a1b3218a672e7b641b464632117b4e91010b49fe103863e2e11ecc6853b4ae", "1.1--pl5321r41hdfd78af_0": "sha256:f94ae66f440a73de7bfa71d9aa4bf342d8d4490d740569166a0b9a198966e4f4", "1.1--pl5321hdfd78af_1": "sha256:dfc18e755aec8d7aa93b9b9896dfe7cfe53853b439c1ca2de248412e340e1d2c", "1.1--pl5321hdfd78af_2": "sha256:e8f4c1b3e3c72c14bea0c1b91639e3be82bd2e4f087ec7e95dbbeb170a60465b"}, "docker": "quay.io/biocontainers/mirnature", "aliases": {"MIRfix.py": "/usr/local/bin/MIRfix.py", "dialign2-2": "/usr/local/bin/dialign2-2", "evaluate_conserved_str.py": "/usr/local/bin/evaluate_conserved_str.py", "miRNAnchor.pl": "/usr/local/bin/miRNAnchor.pl", "miRNAture": "/usr/local/bin/miRNAture", "miRNAture.pl": "/usr/local/bin/miRNAture.pl", "runMIRfix.sh": "/usr/local/bin/runMIRfix.sh", "testMIRfix.sh": "/usr/local/bin/testMIRfix.sh", "rmblastn": "/usr/local/bin/rmblastn", "clustalo": "/usr/local/bin/clustalo", "blast_report": "/usr/local/bin/blast_report", "blastdb_convert": "/usr/local/bin/blastdb_convert", "blastdb_path": "/usr/local/bin/blastdb_path", "bl2seq": "/usr/local/bin/bl2seq", "blastall": "/usr/local/bin/blastall", "blastclust": "/usr/local/bin/blastclust", "blastpgp": "/usr/local/bin/blastpgp", "copymat": "/usr/local/bin/copymat"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/mirnature.
shpc-registry automated BioContainers addition for mirnature
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/mirnature
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/mirnature:1.1--pl5321hdfd78af_2
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/mirnature/1.1--pl5321hdfd78af_2
$ module help quay.io/biocontainers/mirnature/1.1--pl5321hdfd78af_2
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### mirnature-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### mirnature-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### mirnature-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### mirnature-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### mirnature-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### mirnature-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### MIRfix.py

```bash
$ singularity exec <container> /usr/local/bin/MIRfix.py
$ podman run --it --rm --entrypoint /usr/local/bin/MIRfix.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/MIRfix.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### dialign2-2

```bash
$ singularity exec <container> /usr/local/bin/dialign2-2
$ podman run --it --rm --entrypoint /usr/local/bin/dialign2-2   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/dialign2-2   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### evaluate_conserved_str.py

```bash
$ singularity exec <container> /usr/local/bin/evaluate_conserved_str.py
$ podman run --it --rm --entrypoint /usr/local/bin/evaluate_conserved_str.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/evaluate_conserved_str.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### miRNAnchor.pl

```bash
$ singularity exec <container> /usr/local/bin/miRNAnchor.pl
$ podman run --it --rm --entrypoint /usr/local/bin/miRNAnchor.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/miRNAnchor.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### miRNAture

```bash
$ singularity exec <container> /usr/local/bin/miRNAture
$ podman run --it --rm --entrypoint /usr/local/bin/miRNAture   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/miRNAture   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### miRNAture.pl

```bash
$ singularity exec <container> /usr/local/bin/miRNAture.pl
$ podman run --it --rm --entrypoint /usr/local/bin/miRNAture.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/miRNAture.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### runMIRfix.sh

```bash
$ singularity exec <container> /usr/local/bin/runMIRfix.sh
$ podman run --it --rm --entrypoint /usr/local/bin/runMIRfix.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/runMIRfix.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### testMIRfix.sh

```bash
$ singularity exec <container> /usr/local/bin/testMIRfix.sh
$ podman run --it --rm --entrypoint /usr/local/bin/testMIRfix.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/testMIRfix.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### rmblastn

```bash
$ singularity exec <container> /usr/local/bin/rmblastn
$ podman run --it --rm --entrypoint /usr/local/bin/rmblastn   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/rmblastn   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### clustalo

```bash
$ singularity exec <container> /usr/local/bin/clustalo
$ podman run --it --rm --entrypoint /usr/local/bin/clustalo   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/clustalo   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### blast_report

```bash
$ singularity exec <container> /usr/local/bin/blast_report
$ podman run --it --rm --entrypoint /usr/local/bin/blast_report   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/blast_report   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### blastdb_convert

```bash
$ singularity exec <container> /usr/local/bin/blastdb_convert
$ podman run --it --rm --entrypoint /usr/local/bin/blastdb_convert   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/blastdb_convert   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### blastdb_path

```bash
$ singularity exec <container> /usr/local/bin/blastdb_path
$ podman run --it --rm --entrypoint /usr/local/bin/blastdb_path   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/blastdb_path   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bl2seq

```bash
$ singularity exec <container> /usr/local/bin/bl2seq
$ podman run --it --rm --entrypoint /usr/local/bin/bl2seq   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bl2seq   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### blastall

```bash
$ singularity exec <container> /usr/local/bin/blastall
$ podman run --it --rm --entrypoint /usr/local/bin/blastall   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/blastall   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### blastclust

```bash
$ singularity exec <container> /usr/local/bin/blastclust
$ podman run --it --rm --entrypoint /usr/local/bin/blastclust   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/blastclust   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### blastpgp

```bash
$ singularity exec <container> /usr/local/bin/blastpgp
$ podman run --it --rm --entrypoint /usr/local/bin/blastpgp   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/blastpgp   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### copymat

```bash
$ singularity exec <container> /usr/local/bin/copymat
$ podman run --it --rm --entrypoint /usr/local/bin/copymat   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/copymat   -v ${PWD} -w ${PWD} <container> -c " $@"
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