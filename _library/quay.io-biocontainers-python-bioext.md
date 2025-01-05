---
layout: container
name:  "quay.io/biocontainers/python-bioext"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/python-bioext/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/python-bioext/container.yaml"
updated_at: "2025-01-05 03:22:28.318074"
latest: "0.21.9--py310ha6711e0_1"
container_url: "https://biocontainers.pro/tools/python-bioext"
aliases:
 - "bam2fna"
 - "bam2msa"
 - "bamclip"
 - "bealign"
 - "clipedge"
 - "consensus"
 - "msa2bam"
 - "seqmerge"
 - "translate"
 - "f2py3.9"
 - "2to3-3.9"
 - "idle3.9"
 - "pydoc3.9"
 - "python3.9"
 - "python3.9-config"
versions:
 - "0.20.4--py39h7f6d023_2"
 - "0.21.2--py38hecf9f4f_0"
 - "0.21.2--py310h748d2df_0"
 - "0.20.4--py310h69358a1_2"
 - "0.21.7--py39h6f52fb9_1"
 - "0.21.8--py39h91a4a08_1"
 - "0.21.9--py39h91a4a08_0"
 - "0.21.9--py310ha6711e0_1"
description: "shpc-registry automated BioContainers addition for python-bioext"
config: {"url": "https://biocontainers.pro/tools/python-bioext", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for python-bioext", "latest": {"0.21.9--py310ha6711e0_1": "sha256:bc4efcfc939c4e3980ba186055aa1e8dff8a517efaa9f9bdeda6b13f4e7fdaa1"}, "tags": {"0.20.4--py39h7f6d023_2": "sha256:da83fe6d4b44b625e96632c11892d4a7d3786c6cd6bc3cce7537811b927e8545", "0.21.2--py38hecf9f4f_0": "sha256:1c2d7bde1c40ae4f1ebb32c4d609399ac6763846d4fe4a85e7ad508ff37ce225", "0.21.2--py310h748d2df_0": "sha256:3b5e61a71c2a16e65405b14d6e2758092f9955046f80a5a5b90843d83ca51afd", "0.20.4--py310h69358a1_2": "sha256:7c5c0c71a0aa4e144def3a5e9c4aa038daf8670188a568157f951ab8e1cff38b", "0.21.7--py39h6f52fb9_1": "sha256:865077de8e40539058c2c4e8cfe57ee9db5fdf1ff4540b5376aa3c5c50be65ba", "0.21.8--py39h91a4a08_1": "sha256:4193042400eadc418314ed3e8a065896239bd98e30c5069f50ac959de8ac3caa", "0.21.9--py39h91a4a08_0": "sha256:5a196c656af210425b71ee975dd0051dfbbb0335981d8e4943a16839430ac154", "0.21.9--py310ha6711e0_1": "sha256:bc4efcfc939c4e3980ba186055aa1e8dff8a517efaa9f9bdeda6b13f4e7fdaa1"}, "docker": "quay.io/biocontainers/python-bioext", "aliases": {"bam2fna": "/usr/local/bin/bam2fna", "bam2msa": "/usr/local/bin/bam2msa", "bamclip": "/usr/local/bin/bamclip", "bealign": "/usr/local/bin/bealign", "clipedge": "/usr/local/bin/clipedge", "consensus": "/usr/local/bin/consensus", "msa2bam": "/usr/local/bin/msa2bam", "seqmerge": "/usr/local/bin/seqmerge", "translate": "/usr/local/bin/translate", "f2py3.9": "/usr/local/bin/f2py3.9", "2to3-3.9": "/usr/local/bin/2to3-3.9", "idle3.9": "/usr/local/bin/idle3.9", "pydoc3.9": "/usr/local/bin/pydoc3.9", "python3.9": "/usr/local/bin/python3.9", "python3.9-config": "/usr/local/bin/python3.9-config"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/python-bioext.
shpc-registry automated BioContainers addition for python-bioext
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/python-bioext
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/python-bioext:0.21.9--py310ha6711e0_1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/python-bioext/0.21.9--py310ha6711e0_1
$ module help quay.io/biocontainers/python-bioext/0.21.9--py310ha6711e0_1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### python-bioext-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### python-bioext-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### python-bioext-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### python-bioext-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### python-bioext-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### python-bioext-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### bam2fna

```bash
$ singularity exec <container> /usr/local/bin/bam2fna
$ podman run --it --rm --entrypoint /usr/local/bin/bam2fna   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bam2fna   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bam2msa

```bash
$ singularity exec <container> /usr/local/bin/bam2msa
$ podman run --it --rm --entrypoint /usr/local/bin/bam2msa   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bam2msa   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bamclip

```bash
$ singularity exec <container> /usr/local/bin/bamclip
$ podman run --it --rm --entrypoint /usr/local/bin/bamclip   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bamclip   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bealign

```bash
$ singularity exec <container> /usr/local/bin/bealign
$ podman run --it --rm --entrypoint /usr/local/bin/bealign   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bealign   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### clipedge

```bash
$ singularity exec <container> /usr/local/bin/clipedge
$ podman run --it --rm --entrypoint /usr/local/bin/clipedge   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/clipedge   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### consensus

```bash
$ singularity exec <container> /usr/local/bin/consensus
$ podman run --it --rm --entrypoint /usr/local/bin/consensus   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/consensus   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### msa2bam

```bash
$ singularity exec <container> /usr/local/bin/msa2bam
$ podman run --it --rm --entrypoint /usr/local/bin/msa2bam   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/msa2bam   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### seqmerge

```bash
$ singularity exec <container> /usr/local/bin/seqmerge
$ podman run --it --rm --entrypoint /usr/local/bin/seqmerge   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/seqmerge   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### translate

```bash
$ singularity exec <container> /usr/local/bin/translate
$ podman run --it --rm --entrypoint /usr/local/bin/translate   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/translate   -v ${PWD} -w ${PWD} <container> -c " $@"
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