---
layout: container
name:  "quay.io/biocontainers/mage-tab-merger"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/mage-tab-merger/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/mage-tab-merger/container.yaml"
updated_at: "2023-03-04 03:02:14.234948"
latest: "0.0.4--pyh5e36f6f_0"
container_url: "https://biocontainers.pro/tools/mage-tab-merger"
aliases:
 - "merge_baseline_configuration_xmls.py"
 - "merge_condensed_sdrfs.py"
 - "merge_data.py"
 - "merge_sdrfs.py"
 - "retrieve_data.py"
 - "chardetect"
 - "f2py3.9"
 - "2to3-3.9"
 - "idle3.9"
 - "pydoc3.9"
 - "python3.9"
 - "python3.9-config"
versions:
 - "0.0.4--pyh5e36f6f_0"
description: "singularity registry hpc automated addition for mage-tab-merger"
config: {"url": "https://biocontainers.pro/tools/mage-tab-merger", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for mage-tab-merger", "latest": {"0.0.4--pyh5e36f6f_0": "sha256:2159089f8af0b07059f0c6101e19642a7b58baa9fadd833d292997236d65c95f"}, "tags": {"0.0.4--pyh5e36f6f_0": "sha256:2159089f8af0b07059f0c6101e19642a7b58baa9fadd833d292997236d65c95f"}, "docker": "quay.io/biocontainers/mage-tab-merger", "aliases": {"merge_baseline_configuration_xmls.py": "/usr/local/bin/merge_baseline_configuration_xmls.py", "merge_condensed_sdrfs.py": "/usr/local/bin/merge_condensed_sdrfs.py", "merge_data.py": "/usr/local/bin/merge_data.py", "merge_sdrfs.py": "/usr/local/bin/merge_sdrfs.py", "retrieve_data.py": "/usr/local/bin/retrieve_data.py", "chardetect": "/usr/local/bin/chardetect", "f2py3.9": "/usr/local/bin/f2py3.9", "2to3-3.9": "/usr/local/bin/2to3-3.9", "idle3.9": "/usr/local/bin/idle3.9", "pydoc3.9": "/usr/local/bin/pydoc3.9", "python3.9": "/usr/local/bin/python3.9", "python3.9-config": "/usr/local/bin/python3.9-config"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/mage-tab-merger.
singularity registry hpc automated addition for mage-tab-merger
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/mage-tab-merger
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/mage-tab-merger:0.0.4--pyh5e36f6f_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/mage-tab-merger/0.0.4--pyh5e36f6f_0
$ module help quay.io/biocontainers/mage-tab-merger/0.0.4--pyh5e36f6f_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### mage-tab-merger-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### mage-tab-merger-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### mage-tab-merger-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### mage-tab-merger-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### mage-tab-merger-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### mage-tab-merger-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### merge_baseline_configuration_xmls.py

```bash
$ singularity exec <container> /usr/local/bin/merge_baseline_configuration_xmls.py
$ podman run --it --rm --entrypoint /usr/local/bin/merge_baseline_configuration_xmls.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/merge_baseline_configuration_xmls.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### merge_condensed_sdrfs.py

```bash
$ singularity exec <container> /usr/local/bin/merge_condensed_sdrfs.py
$ podman run --it --rm --entrypoint /usr/local/bin/merge_condensed_sdrfs.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/merge_condensed_sdrfs.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### merge_data.py

```bash
$ singularity exec <container> /usr/local/bin/merge_data.py
$ podman run --it --rm --entrypoint /usr/local/bin/merge_data.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/merge_data.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### merge_sdrfs.py

```bash
$ singularity exec <container> /usr/local/bin/merge_sdrfs.py
$ podman run --it --rm --entrypoint /usr/local/bin/merge_sdrfs.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/merge_sdrfs.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### retrieve_data.py

```bash
$ singularity exec <container> /usr/local/bin/retrieve_data.py
$ podman run --it --rm --entrypoint /usr/local/bin/retrieve_data.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/retrieve_data.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### chardetect

```bash
$ singularity exec <container> /usr/local/bin/chardetect
$ podman run --it --rm --entrypoint /usr/local/bin/chardetect   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/chardetect   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### f2py3.9

```bash
$ singularity exec <container> /usr/local/bin/f2py3.9
$ podman run --it --rm --entrypoint /usr/local/bin/f2py3.9   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/f2py3.9   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### 2to3-3.9

```bash
$ singularity exec <container> /usr/local/bin/2to3-3.9
$ podman run --it --rm --entrypoint /usr/local/bin/2to3-3.9   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/2to3-3.9   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### idle3.9

```bash
$ singularity exec <container> /usr/local/bin/idle3.9
$ podman run --it --rm --entrypoint /usr/local/bin/idle3.9   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/idle3.9   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pydoc3.9

```bash
$ singularity exec <container> /usr/local/bin/pydoc3.9
$ podman run --it --rm --entrypoint /usr/local/bin/pydoc3.9   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pydoc3.9   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python3.9

```bash
$ singularity exec <container> /usr/local/bin/python3.9
$ podman run --it --rm --entrypoint /usr/local/bin/python3.9   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python3.9   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python3.9-config

```bash
$ singularity exec <container> /usr/local/bin/python3.9-config
$ podman run --it --rm --entrypoint /usr/local/bin/python3.9-config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python3.9-config   -v ${PWD} -w ${PWD} <container> -c " $@"
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