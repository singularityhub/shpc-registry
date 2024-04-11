---
layout: container
name:  "quay.io/biocontainers/docking_py"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/docking_py/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/docking_py/container.yaml"
updated_at: "2024-04-11 02:41:19.623327"
latest: "0.2.3--py_0"
container_url: "https://biocontainers.pro/tools/docking_py"
aliases:
 - "adt"
 - "archosv"
 - "cadd"
 - "docking_py"
 - "mglenv.csh"
 - "mglenv.sh"
 - "pdb2pqr_cli"
 - "pmv"
 - "prepare_ligand4.py"
 - "prepare_receptor4.py"
 - "python2.5"
 - "python2.5-config"
 - "pythonsh"
 - "qvina2"
 - "qvina2_split"
 - "qvinaw"
 - "qvinaw_split"
 - "smina"
 - "tester"
 - "vina"
 - "vina_split"
 - "vision"
 - "pilconvert.py"
 - "pildriver.py"
 - "pilfile.py"
 - "pilfont.py"
 - "pilprint.py"
 - "f2py3.8"
 - "idle"
 - "python-config"
 - "smtpd.py"
 - "2to3-3.8"
versions:
 - "0.2.3--py_0"
description: "shpc-registry automated BioContainers addition for docking_py"
config: {"url": "https://biocontainers.pro/tools/docking_py", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for docking_py", "latest": {"0.2.3--py_0": "sha256:8003521478c3922aaca3cf98f9e34463e25871637d19bc08eb3109934e145b9c"}, "tags": {"0.2.3--py_0": "sha256:8003521478c3922aaca3cf98f9e34463e25871637d19bc08eb3109934e145b9c"}, "docker": "quay.io/biocontainers/docking_py", "aliases": {"adt": "/usr/local/bin/adt", "archosv": "/usr/local/bin/archosv", "cadd": "/usr/local/bin/cadd", "docking_py": "/usr/local/bin/docking_py", "mglenv.csh": "/usr/local/bin/mglenv.csh", "mglenv.sh": "/usr/local/bin/mglenv.sh", "pdb2pqr_cli": "/usr/local/bin/pdb2pqr_cli", "pmv": "/usr/local/bin/pmv", "prepare_ligand4.py": "/usr/local/bin/prepare_ligand4.py", "prepare_receptor4.py": "/usr/local/bin/prepare_receptor4.py", "python2.5": "/usr/local/bin/python2.5", "python2.5-config": "/usr/local/bin/python2.5-config", "pythonsh": "/usr/local/bin/pythonsh", "qvina2": "/usr/local/bin/qvina2", "qvina2_split": "/usr/local/bin/qvina2_split", "qvinaw": "/usr/local/bin/qvinaw", "qvinaw_split": "/usr/local/bin/qvinaw_split", "smina": "/usr/local/bin/smina", "tester": "/usr/local/bin/tester", "vina": "/usr/local/bin/vina", "vina_split": "/usr/local/bin/vina_split", "vision": "/usr/local/bin/vision", "pilconvert.py": "/usr/local/bin/pilconvert.py", "pildriver.py": "/usr/local/bin/pildriver.py", "pilfile.py": "/usr/local/bin/pilfile.py", "pilfont.py": "/usr/local/bin/pilfont.py", "pilprint.py": "/usr/local/bin/pilprint.py", "f2py3.8": "/usr/local/bin/f2py3.8", "idle": "/usr/local/bin/idle", "python-config": "/usr/local/bin/python-config", "smtpd.py": "/usr/local/bin/smtpd.py", "2to3-3.8": "/usr/local/bin/2to3-3.8"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/docking_py.
shpc-registry automated BioContainers addition for docking_py
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/docking_py
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/docking_py:0.2.3--py_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/docking_py/0.2.3--py_0
$ module help quay.io/biocontainers/docking_py/0.2.3--py_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### docking_py-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### docking_py-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### docking_py-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### docking_py-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### docking_py-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### docking_py-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### adt

```bash
$ singularity exec <container> /usr/local/bin/adt
$ podman run --it --rm --entrypoint /usr/local/bin/adt   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/adt   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### archosv

```bash
$ singularity exec <container> /usr/local/bin/archosv
$ podman run --it --rm --entrypoint /usr/local/bin/archosv   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/archosv   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### cadd

```bash
$ singularity exec <container> /usr/local/bin/cadd
$ podman run --it --rm --entrypoint /usr/local/bin/cadd   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cadd   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### docking_py

```bash
$ singularity exec <container> /usr/local/bin/docking_py
$ podman run --it --rm --entrypoint /usr/local/bin/docking_py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/docking_py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mglenv.csh

```bash
$ singularity exec <container> /usr/local/bin/mglenv.csh
$ podman run --it --rm --entrypoint /usr/local/bin/mglenv.csh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mglenv.csh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mglenv.sh

```bash
$ singularity exec <container> /usr/local/bin/mglenv.sh
$ podman run --it --rm --entrypoint /usr/local/bin/mglenv.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mglenv.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pdb2pqr_cli

```bash
$ singularity exec <container> /usr/local/bin/pdb2pqr_cli
$ podman run --it --rm --entrypoint /usr/local/bin/pdb2pqr_cli   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pdb2pqr_cli   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pmv

```bash
$ singularity exec <container> /usr/local/bin/pmv
$ podman run --it --rm --entrypoint /usr/local/bin/pmv   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pmv   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### prepare_ligand4.py

```bash
$ singularity exec <container> /usr/local/bin/prepare_ligand4.py
$ podman run --it --rm --entrypoint /usr/local/bin/prepare_ligand4.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/prepare_ligand4.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### prepare_receptor4.py

```bash
$ singularity exec <container> /usr/local/bin/prepare_receptor4.py
$ podman run --it --rm --entrypoint /usr/local/bin/prepare_receptor4.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/prepare_receptor4.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python2.5

```bash
$ singularity exec <container> /usr/local/bin/python2.5
$ podman run --it --rm --entrypoint /usr/local/bin/python2.5   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python2.5   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python2.5-config

```bash
$ singularity exec <container> /usr/local/bin/python2.5-config
$ podman run --it --rm --entrypoint /usr/local/bin/python2.5-config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python2.5-config   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pythonsh

```bash
$ singularity exec <container> /usr/local/bin/pythonsh
$ podman run --it --rm --entrypoint /usr/local/bin/pythonsh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pythonsh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### qvina2

```bash
$ singularity exec <container> /usr/local/bin/qvina2
$ podman run --it --rm --entrypoint /usr/local/bin/qvina2   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/qvina2   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### qvina2_split

```bash
$ singularity exec <container> /usr/local/bin/qvina2_split
$ podman run --it --rm --entrypoint /usr/local/bin/qvina2_split   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/qvina2_split   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### qvinaw

```bash
$ singularity exec <container> /usr/local/bin/qvinaw
$ podman run --it --rm --entrypoint /usr/local/bin/qvinaw   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/qvinaw   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### qvinaw_split

```bash
$ singularity exec <container> /usr/local/bin/qvinaw_split
$ podman run --it --rm --entrypoint /usr/local/bin/qvinaw_split   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/qvinaw_split   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### smina

```bash
$ singularity exec <container> /usr/local/bin/smina
$ podman run --it --rm --entrypoint /usr/local/bin/smina   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/smina   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### tester

```bash
$ singularity exec <container> /usr/local/bin/tester
$ podman run --it --rm --entrypoint /usr/local/bin/tester   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/tester   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### vina

```bash
$ singularity exec <container> /usr/local/bin/vina
$ podman run --it --rm --entrypoint /usr/local/bin/vina   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/vina   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### vina_split

```bash
$ singularity exec <container> /usr/local/bin/vina_split
$ podman run --it --rm --entrypoint /usr/local/bin/vina_split   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/vina_split   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### vision

```bash
$ singularity exec <container> /usr/local/bin/vision
$ podman run --it --rm --entrypoint /usr/local/bin/vision   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/vision   -v ${PWD} -w ${PWD} <container> -c " $@"
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


#### pilfile.py

```bash
$ singularity exec <container> /usr/local/bin/pilfile.py
$ podman run --it --rm --entrypoint /usr/local/bin/pilfile.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pilfile.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pilfont.py

```bash
$ singularity exec <container> /usr/local/bin/pilfont.py
$ podman run --it --rm --entrypoint /usr/local/bin/pilfont.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pilfont.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pilprint.py

```bash
$ singularity exec <container> /usr/local/bin/pilprint.py
$ podman run --it --rm --entrypoint /usr/local/bin/pilprint.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pilprint.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### f2py3.8

```bash
$ singularity exec <container> /usr/local/bin/f2py3.8
$ podman run --it --rm --entrypoint /usr/local/bin/f2py3.8   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/f2py3.8   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### idle

```bash
$ singularity exec <container> /usr/local/bin/idle
$ podman run --it --rm --entrypoint /usr/local/bin/idle   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/idle   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python-config

```bash
$ singularity exec <container> /usr/local/bin/python-config
$ podman run --it --rm --entrypoint /usr/local/bin/python-config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python-config   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### smtpd.py

```bash
$ singularity exec <container> /usr/local/bin/smtpd.py
$ podman run --it --rm --entrypoint /usr/local/bin/smtpd.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/smtpd.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### 2to3-3.8

```bash
$ singularity exec <container> /usr/local/bin/2to3-3.8
$ podman run --it --rm --entrypoint /usr/local/bin/2to3-3.8   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/2to3-3.8   -v ${PWD} -w ${PWD} <container> -c " $@"
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