---
layout: container
name:  "quay.io/biocontainers/cami-opal"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/cami-opal/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/cami-opal/container.yaml"
updated_at: "2023-08-17 02:56:30.986100"
latest: "1.0.11--pyhdfd78af_0"
container_url: "https://biocontainers.pro/tools/cami-opal"
aliases:
 - "opal.py"
 - "opal_stats.py"
 - "opal_workflow.py"
 - "setup.py"
 - "version.py"
 - "wsdump.py"
 - "dendropy-format"
 - "doesitcache"
 - "iptest3"
 - "bokeh"
 - "sumlabels.py"
 - "sumtrees.py"
 - "iptest"
 - "ipython3"
 - "ipython"
 - "cygdb"
versions:
 - "1.0.9--pyhdfd78af_1"
 - "1.0.11--pyhdfd78af_0"
description: "shpc-registry automated BioContainers addition for cami-opal"
config: {"url": "https://biocontainers.pro/tools/cami-opal", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for cami-opal", "latest": {"1.0.11--pyhdfd78af_0": "sha256:dae974d094d75e49147279d393a633b24a52d71f7cec3b4d82734448b266a58c"}, "tags": {"1.0.9--pyhdfd78af_1": "sha256:51a714b227dfa994fa5f812ad4ac465f15b53c1ad251603d2163e53de1bb0e5d", "1.0.11--pyhdfd78af_0": "sha256:dae974d094d75e49147279d393a633b24a52d71f7cec3b4d82734448b266a58c"}, "docker": "quay.io/biocontainers/cami-opal", "aliases": {"opal.py": "/usr/local/bin/opal.py", "opal_stats.py": "/usr/local/bin/opal_stats.py", "opal_workflow.py": "/usr/local/bin/opal_workflow.py", "setup.py": "/usr/local/bin/setup.py", "version.py": "/usr/local/bin/version.py", "wsdump.py": "/usr/local/bin/wsdump.py", "dendropy-format": "/usr/local/bin/dendropy-format", "doesitcache": "/usr/local/bin/doesitcache", "iptest3": "/usr/local/bin/iptest3", "bokeh": "/usr/local/bin/bokeh", "sumlabels.py": "/usr/local/bin/sumlabels.py", "sumtrees.py": "/usr/local/bin/sumtrees.py", "iptest": "/usr/local/bin/iptest", "ipython3": "/usr/local/bin/ipython3", "ipython": "/usr/local/bin/ipython", "cygdb": "/usr/local/bin/cygdb"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/cami-opal.
shpc-registry automated BioContainers addition for cami-opal
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/cami-opal
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/cami-opal:1.0.11--pyhdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/cami-opal/1.0.11--pyhdfd78af_0
$ module help quay.io/biocontainers/cami-opal/1.0.11--pyhdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### cami-opal-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### cami-opal-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### cami-opal-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### cami-opal-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### cami-opal-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### cami-opal-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### opal.py

```bash
$ singularity exec <container> /usr/local/bin/opal.py
$ podman run --it --rm --entrypoint /usr/local/bin/opal.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/opal.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### opal_stats.py

```bash
$ singularity exec <container> /usr/local/bin/opal_stats.py
$ podman run --it --rm --entrypoint /usr/local/bin/opal_stats.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/opal_stats.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### opal_workflow.py

```bash
$ singularity exec <container> /usr/local/bin/opal_workflow.py
$ podman run --it --rm --entrypoint /usr/local/bin/opal_workflow.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/opal_workflow.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### setup.py

```bash
$ singularity exec <container> /usr/local/bin/setup.py
$ podman run --it --rm --entrypoint /usr/local/bin/setup.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/setup.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### version.py

```bash
$ singularity exec <container> /usr/local/bin/version.py
$ podman run --it --rm --entrypoint /usr/local/bin/version.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/version.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### wsdump.py

```bash
$ singularity exec <container> /usr/local/bin/wsdump.py
$ podman run --it --rm --entrypoint /usr/local/bin/wsdump.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/wsdump.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### dendropy-format

```bash
$ singularity exec <container> /usr/local/bin/dendropy-format
$ podman run --it --rm --entrypoint /usr/local/bin/dendropy-format   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/dendropy-format   -v ${PWD} -w ${PWD} <container> -c " $@"
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


#### bokeh

```bash
$ singularity exec <container> /usr/local/bin/bokeh
$ podman run --it --rm --entrypoint /usr/local/bin/bokeh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bokeh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### sumlabels.py

```bash
$ singularity exec <container> /usr/local/bin/sumlabels.py
$ podman run --it --rm --entrypoint /usr/local/bin/sumlabels.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/sumlabels.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### sumtrees.py

```bash
$ singularity exec <container> /usr/local/bin/sumtrees.py
$ podman run --it --rm --entrypoint /usr/local/bin/sumtrees.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/sumtrees.py   -v ${PWD} -w ${PWD} <container> -c " $@"
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