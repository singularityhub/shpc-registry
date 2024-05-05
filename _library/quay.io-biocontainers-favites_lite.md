---
layout: container
name:  "quay.io/biocontainers/favites_lite"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/favites_lite/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/favites_lite/container.yaml"
updated_at: "2024-05-05 02:37:33.300927"
latest: "1.0.1--hdfd78af_0"
container_url: "https://biocontainers.pro/tools/favites_lite"
aliases:
 - "GEMF"
 - "GEMF_FAVITES.py"
 - "coatran_constant"
 - "coatran_expgrowth"
 - "coatran_inftime"
 - "coatran_transtree"
 - "favites_lite.py"
 - "ngg_barabasi_albert"
 - "ngg_barbell"
 - "ngg_complete"
 - "ngg_cycle"
 - "ngg_empty"
 - "ngg_erdos_renyi"
 - "ngg_newman_watts_strogatz"
 - "ngg_path"
 - "ngg_ring_lattice"
 - "seq-gen"
 - "2to3-3.12"
 - "idle3.12"
 - "pydoc3.12"
 - "python3.12"
 - "python3.12-config"
versions:
 - "1.0.1--hdfd78af_0"
description: "singularity registry hpc automated addition for favites_lite"
config: {"url": "https://biocontainers.pro/tools/favites_lite", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for favites_lite", "latest": {"1.0.1--hdfd78af_0": "sha256:91e448a45956d134b4a250652c7cb17b7cc231eb26d1e30c5d0a53f9e429789e"}, "tags": {"1.0.1--hdfd78af_0": "sha256:91e448a45956d134b4a250652c7cb17b7cc231eb26d1e30c5d0a53f9e429789e"}, "docker": "quay.io/biocontainers/favites_lite", "aliases": {"GEMF": "/usr/local/bin/GEMF", "GEMF_FAVITES.py": "/usr/local/bin/GEMF_FAVITES.py", "coatran_constant": "/usr/local/bin/coatran_constant", "coatran_expgrowth": "/usr/local/bin/coatran_expgrowth", "coatran_inftime": "/usr/local/bin/coatran_inftime", "coatran_transtree": "/usr/local/bin/coatran_transtree", "favites_lite.py": "/usr/local/bin/favites_lite.py", "ngg_barabasi_albert": "/usr/local/bin/ngg_barabasi_albert", "ngg_barbell": "/usr/local/bin/ngg_barbell", "ngg_complete": "/usr/local/bin/ngg_complete", "ngg_cycle": "/usr/local/bin/ngg_cycle", "ngg_empty": "/usr/local/bin/ngg_empty", "ngg_erdos_renyi": "/usr/local/bin/ngg_erdos_renyi", "ngg_newman_watts_strogatz": "/usr/local/bin/ngg_newman_watts_strogatz", "ngg_path": "/usr/local/bin/ngg_path", "ngg_ring_lattice": "/usr/local/bin/ngg_ring_lattice", "seq-gen": "/usr/local/bin/seq-gen", "2to3-3.12": "/usr/local/bin/2to3-3.12", "idle3.12": "/usr/local/bin/idle3.12", "pydoc3.12": "/usr/local/bin/pydoc3.12", "python3.12": "/usr/local/bin/python3.12", "python3.12-config": "/usr/local/bin/python3.12-config"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/favites_lite.
singularity registry hpc automated addition for favites_lite
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/favites_lite
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/favites_lite:1.0.1--hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/favites_lite/1.0.1--hdfd78af_0
$ module help quay.io/biocontainers/favites_lite/1.0.1--hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### favites_lite-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### favites_lite-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### favites_lite-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### favites_lite-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### favites_lite-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### favites_lite-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### GEMF

```bash
$ singularity exec <container> /usr/local/bin/GEMF
$ podman run --it --rm --entrypoint /usr/local/bin/GEMF   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/GEMF   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### GEMF_FAVITES.py

```bash
$ singularity exec <container> /usr/local/bin/GEMF_FAVITES.py
$ podman run --it --rm --entrypoint /usr/local/bin/GEMF_FAVITES.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/GEMF_FAVITES.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### coatran_constant

```bash
$ singularity exec <container> /usr/local/bin/coatran_constant
$ podman run --it --rm --entrypoint /usr/local/bin/coatran_constant   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/coatran_constant   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### coatran_expgrowth

```bash
$ singularity exec <container> /usr/local/bin/coatran_expgrowth
$ podman run --it --rm --entrypoint /usr/local/bin/coatran_expgrowth   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/coatran_expgrowth   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### coatran_inftime

```bash
$ singularity exec <container> /usr/local/bin/coatran_inftime
$ podman run --it --rm --entrypoint /usr/local/bin/coatran_inftime   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/coatran_inftime   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### coatran_transtree

```bash
$ singularity exec <container> /usr/local/bin/coatran_transtree
$ podman run --it --rm --entrypoint /usr/local/bin/coatran_transtree   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/coatran_transtree   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### favites_lite.py

```bash
$ singularity exec <container> /usr/local/bin/favites_lite.py
$ podman run --it --rm --entrypoint /usr/local/bin/favites_lite.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/favites_lite.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ngg_barabasi_albert

```bash
$ singularity exec <container> /usr/local/bin/ngg_barabasi_albert
$ podman run --it --rm --entrypoint /usr/local/bin/ngg_barabasi_albert   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ngg_barabasi_albert   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ngg_barbell

```bash
$ singularity exec <container> /usr/local/bin/ngg_barbell
$ podman run --it --rm --entrypoint /usr/local/bin/ngg_barbell   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ngg_barbell   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ngg_complete

```bash
$ singularity exec <container> /usr/local/bin/ngg_complete
$ podman run --it --rm --entrypoint /usr/local/bin/ngg_complete   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ngg_complete   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ngg_cycle

```bash
$ singularity exec <container> /usr/local/bin/ngg_cycle
$ podman run --it --rm --entrypoint /usr/local/bin/ngg_cycle   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ngg_cycle   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ngg_empty

```bash
$ singularity exec <container> /usr/local/bin/ngg_empty
$ podman run --it --rm --entrypoint /usr/local/bin/ngg_empty   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ngg_empty   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ngg_erdos_renyi

```bash
$ singularity exec <container> /usr/local/bin/ngg_erdos_renyi
$ podman run --it --rm --entrypoint /usr/local/bin/ngg_erdos_renyi   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ngg_erdos_renyi   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ngg_newman_watts_strogatz

```bash
$ singularity exec <container> /usr/local/bin/ngg_newman_watts_strogatz
$ podman run --it --rm --entrypoint /usr/local/bin/ngg_newman_watts_strogatz   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ngg_newman_watts_strogatz   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ngg_path

```bash
$ singularity exec <container> /usr/local/bin/ngg_path
$ podman run --it --rm --entrypoint /usr/local/bin/ngg_path   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ngg_path   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ngg_ring_lattice

```bash
$ singularity exec <container> /usr/local/bin/ngg_ring_lattice
$ podman run --it --rm --entrypoint /usr/local/bin/ngg_ring_lattice   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ngg_ring_lattice   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### seq-gen

```bash
$ singularity exec <container> /usr/local/bin/seq-gen
$ podman run --it --rm --entrypoint /usr/local/bin/seq-gen   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/seq-gen   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### 2to3-3.12

```bash
$ singularity exec <container> /usr/local/bin/2to3-3.12
$ podman run --it --rm --entrypoint /usr/local/bin/2to3-3.12   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/2to3-3.12   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### idle3.12

```bash
$ singularity exec <container> /usr/local/bin/idle3.12
$ podman run --it --rm --entrypoint /usr/local/bin/idle3.12   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/idle3.12   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pydoc3.12

```bash
$ singularity exec <container> /usr/local/bin/pydoc3.12
$ podman run --it --rm --entrypoint /usr/local/bin/pydoc3.12   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pydoc3.12   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python3.12

```bash
$ singularity exec <container> /usr/local/bin/python3.12
$ podman run --it --rm --entrypoint /usr/local/bin/python3.12   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python3.12   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python3.12-config

```bash
$ singularity exec <container> /usr/local/bin/python3.12-config
$ podman run --it --rm --entrypoint /usr/local/bin/python3.12-config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python3.12-config   -v ${PWD} -w ${PWD} <container> -c " $@"
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