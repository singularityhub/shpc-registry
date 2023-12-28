---
layout: container
name:  "quay.io/biocontainers/scnic"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/scnic/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/scnic/container.yaml"
updated_at: "2023-12-28 02:37:04.937381"
latest: "0.6.3--pyhdfd78af_0"
container_url: "https://biocontainers.pro/tools/scnic"
aliases:
 - "SCNIC_analysis.py"
 - "fastspar"
 - "fastspar_bootstrap"
 - "fastspar_pvalues"
 - "fastspar_reduce"
 - "module_enrichment.py"
 - "biom"
 - "doesitcache"
 - "iptest3"
 - "iptest"
 - "ipython3"
 - "ipython"
 - "cygdb"
 - "cython"
 - "cythonize"
 - "py.test"
versions:
 - "0.6.2--py_0"
 - "0.6.3--pyhdfd78af_0"
description: "shpc-registry automated BioContainers addition for scnic"
config: {"url": "https://biocontainers.pro/tools/scnic", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for scnic", "latest": {"0.6.3--pyhdfd78af_0": "sha256:c028a9686991806c8f2bae83898bf072365686edcacffc9003b6616f3168cd0c"}, "tags": {"0.6.2--py_0": "sha256:94503fffd20fed02d570402120ad007ce339ceb533ac22eabe3d4e7ca4c6c426", "0.6.3--pyhdfd78af_0": "sha256:c028a9686991806c8f2bae83898bf072365686edcacffc9003b6616f3168cd0c"}, "docker": "quay.io/biocontainers/scnic", "aliases": {"SCNIC_analysis.py": "/usr/local/bin/SCNIC_analysis.py", "fastspar": "/usr/local/bin/fastspar", "fastspar_bootstrap": "/usr/local/bin/fastspar_bootstrap", "fastspar_pvalues": "/usr/local/bin/fastspar_pvalues", "fastspar_reduce": "/usr/local/bin/fastspar_reduce", "module_enrichment.py": "/usr/local/bin/module_enrichment.py", "biom": "/usr/local/bin/biom", "doesitcache": "/usr/local/bin/doesitcache", "iptest3": "/usr/local/bin/iptest3", "iptest": "/usr/local/bin/iptest", "ipython3": "/usr/local/bin/ipython3", "ipython": "/usr/local/bin/ipython", "cygdb": "/usr/local/bin/cygdb", "cython": "/usr/local/bin/cython", "cythonize": "/usr/local/bin/cythonize", "py.test": "/usr/local/bin/py.test"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/scnic.
shpc-registry automated BioContainers addition for scnic
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/scnic
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/scnic:0.6.3--pyhdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/scnic/0.6.3--pyhdfd78af_0
$ module help quay.io/biocontainers/scnic/0.6.3--pyhdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### scnic-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### scnic-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### scnic-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### scnic-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### scnic-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### scnic-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### SCNIC_analysis.py

```bash
$ singularity exec <container> /usr/local/bin/SCNIC_analysis.py
$ podman run --it --rm --entrypoint /usr/local/bin/SCNIC_analysis.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/SCNIC_analysis.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fastspar

```bash
$ singularity exec <container> /usr/local/bin/fastspar
$ podman run --it --rm --entrypoint /usr/local/bin/fastspar   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fastspar   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fastspar_bootstrap

```bash
$ singularity exec <container> /usr/local/bin/fastspar_bootstrap
$ podman run --it --rm --entrypoint /usr/local/bin/fastspar_bootstrap   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fastspar_bootstrap   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fastspar_pvalues

```bash
$ singularity exec <container> /usr/local/bin/fastspar_pvalues
$ podman run --it --rm --entrypoint /usr/local/bin/fastspar_pvalues   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fastspar_pvalues   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fastspar_reduce

```bash
$ singularity exec <container> /usr/local/bin/fastspar_reduce
$ podman run --it --rm --entrypoint /usr/local/bin/fastspar_reduce   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fastspar_reduce   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### module_enrichment.py

```bash
$ singularity exec <container> /usr/local/bin/module_enrichment.py
$ podman run --it --rm --entrypoint /usr/local/bin/module_enrichment.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/module_enrichment.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### biom

```bash
$ singularity exec <container> /usr/local/bin/biom
$ podman run --it --rm --entrypoint /usr/local/bin/biom   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/biom   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### doesitcache

```bash
$ singularity exec <container> /usr/local/bin/doesitcache
$ podman run --it --rm --entrypoint /usr/local/bin/doesitcache   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/doesitcache   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### iptest3

```bash
$ singularity exec <container> /usr/local/bin/iptest3
$ podman run --it --rm --entrypoint /usr/local/bin/iptest3   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/iptest3   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### iptest

```bash
$ singularity exec <container> /usr/local/bin/iptest
$ podman run --it --rm --entrypoint /usr/local/bin/iptest   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/iptest   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ipython3

```bash
$ singularity exec <container> /usr/local/bin/ipython3
$ podman run --it --rm --entrypoint /usr/local/bin/ipython3   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ipython3   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ipython

```bash
$ singularity exec <container> /usr/local/bin/ipython
$ podman run --it --rm --entrypoint /usr/local/bin/ipython   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ipython   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### cygdb

```bash
$ singularity exec <container> /usr/local/bin/cygdb
$ podman run --it --rm --entrypoint /usr/local/bin/cygdb   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cygdb   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### cython

```bash
$ singularity exec <container> /usr/local/bin/cython
$ podman run --it --rm --entrypoint /usr/local/bin/cython   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cython   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### cythonize

```bash
$ singularity exec <container> /usr/local/bin/cythonize
$ podman run --it --rm --entrypoint /usr/local/bin/cythonize   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cythonize   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### py.test

```bash
$ singularity exec <container> /usr/local/bin/py.test
$ podman run --it --rm --entrypoint /usr/local/bin/py.test   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/py.test   -v ${PWD} -w ${PWD} <container> -c " $@"
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