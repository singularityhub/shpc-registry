---
layout: container
name:  "quay.io/biocontainers/biobb_pmx"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/biobb_pmx/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/biobb_pmx/container.yaml"
updated_at: "2022-11-27 12:11:06.225737"
latest: "3.8.1--pyhdfd78af_0"
container_url: "https://biocontainers.pro/tools/biobb_pmx"
aliases:
 - "pmx"
 - "pmxanalyse"
 - "pmxatom_mapping"
 - "pmxcreate_top"
 - "pmxgentop"
 - "pmxligand_hybrid"
 - "pmxmerge_ff"
 - "pmxmutate"
 - "fonttools"
 - "pyftmerge"
 - "pyftsubset"
 - "ttx"
 - "normalizer"
 - "brotli"
 - "futurize"
 - "pasteurize"
 - "f2py3.7"
 - "opj_compress"
versions:
 - "3.8.1--pyhdfd78af_0"
description: "shpc-registry automated BioContainers addition for biobb_pmx"
config: {"url": "https://biocontainers.pro/tools/biobb_pmx", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for biobb_pmx", "latest": {"3.8.1--pyhdfd78af_0": "sha256:c25e06f154b5294239498065229e08b4dc736a2f3a0f81cc67d0632d57007b78"}, "tags": {"3.8.1--pyhdfd78af_0": "sha256:c25e06f154b5294239498065229e08b4dc736a2f3a0f81cc67d0632d57007b78"}, "docker": "quay.io/biocontainers/biobb_pmx", "aliases": {"pmx": "/usr/local/bin/pmx", "pmxanalyse": "/usr/local/bin/pmxanalyse", "pmxatom_mapping": "/usr/local/bin/pmxatom_mapping", "pmxcreate_top": "/usr/local/bin/pmxcreate_top", "pmxgentop": "/usr/local/bin/pmxgentop", "pmxligand_hybrid": "/usr/local/bin/pmxligand_hybrid", "pmxmerge_ff": "/usr/local/bin/pmxmerge_ff", "pmxmutate": "/usr/local/bin/pmxmutate", "fonttools": "/usr/local/bin/fonttools", "pyftmerge": "/usr/local/bin/pyftmerge", "pyftsubset": "/usr/local/bin/pyftsubset", "ttx": "/usr/local/bin/ttx", "normalizer": "/usr/local/bin/normalizer", "brotli": "/usr/local/bin/brotli", "futurize": "/usr/local/bin/futurize", "pasteurize": "/usr/local/bin/pasteurize", "f2py3.7": "/usr/local/bin/f2py3.7", "opj_compress": "/usr/local/bin/opj_compress"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/biobb_pmx.
shpc-registry automated BioContainers addition for biobb_pmx
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/biobb_pmx
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/biobb_pmx:3.8.1--pyhdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/biobb_pmx/3.8.1--pyhdfd78af_0
$ module help quay.io/biocontainers/biobb_pmx/3.8.1--pyhdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### biobb_pmx-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### biobb_pmx-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### biobb_pmx-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### biobb_pmx-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### biobb_pmx-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### biobb_pmx-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### pmx

```bash
$ singularity exec <container> /usr/local/bin/pmx
$ podman run --it --rm --entrypoint /usr/local/bin/pmx   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pmx   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pmxanalyse

```bash
$ singularity exec <container> /usr/local/bin/pmxanalyse
$ podman run --it --rm --entrypoint /usr/local/bin/pmxanalyse   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pmxanalyse   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pmxatom_mapping

```bash
$ singularity exec <container> /usr/local/bin/pmxatom_mapping
$ podman run --it --rm --entrypoint /usr/local/bin/pmxatom_mapping   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pmxatom_mapping   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pmxcreate_top

```bash
$ singularity exec <container> /usr/local/bin/pmxcreate_top
$ podman run --it --rm --entrypoint /usr/local/bin/pmxcreate_top   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pmxcreate_top   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pmxgentop

```bash
$ singularity exec <container> /usr/local/bin/pmxgentop
$ podman run --it --rm --entrypoint /usr/local/bin/pmxgentop   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pmxgentop   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pmxligand_hybrid

```bash
$ singularity exec <container> /usr/local/bin/pmxligand_hybrid
$ podman run --it --rm --entrypoint /usr/local/bin/pmxligand_hybrid   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pmxligand_hybrid   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pmxmerge_ff

```bash
$ singularity exec <container> /usr/local/bin/pmxmerge_ff
$ podman run --it --rm --entrypoint /usr/local/bin/pmxmerge_ff   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pmxmerge_ff   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pmxmutate

```bash
$ singularity exec <container> /usr/local/bin/pmxmutate
$ podman run --it --rm --entrypoint /usr/local/bin/pmxmutate   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pmxmutate   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fonttools

```bash
$ singularity exec <container> /usr/local/bin/fonttools
$ podman run --it --rm --entrypoint /usr/local/bin/fonttools   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fonttools   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pyftmerge

```bash
$ singularity exec <container> /usr/local/bin/pyftmerge
$ podman run --it --rm --entrypoint /usr/local/bin/pyftmerge   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pyftmerge   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pyftsubset

```bash
$ singularity exec <container> /usr/local/bin/pyftsubset
$ podman run --it --rm --entrypoint /usr/local/bin/pyftsubset   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pyftsubset   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ttx

```bash
$ singularity exec <container> /usr/local/bin/ttx
$ podman run --it --rm --entrypoint /usr/local/bin/ttx   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ttx   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### normalizer

```bash
$ singularity exec <container> /usr/local/bin/normalizer
$ podman run --it --rm --entrypoint /usr/local/bin/normalizer   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/normalizer   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### brotli

```bash
$ singularity exec <container> /usr/local/bin/brotli
$ podman run --it --rm --entrypoint /usr/local/bin/brotli   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/brotli   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### futurize

```bash
$ singularity exec <container> /usr/local/bin/futurize
$ podman run --it --rm --entrypoint /usr/local/bin/futurize   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/futurize   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pasteurize

```bash
$ singularity exec <container> /usr/local/bin/pasteurize
$ podman run --it --rm --entrypoint /usr/local/bin/pasteurize   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pasteurize   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### f2py3.7

```bash
$ singularity exec <container> /usr/local/bin/f2py3.7
$ podman run --it --rm --entrypoint /usr/local/bin/f2py3.7   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/f2py3.7   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### opj_compress

```bash
$ singularity exec <container> /usr/local/bin/opj_compress
$ podman run --it --rm --entrypoint /usr/local/bin/opj_compress   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/opj_compress   -v ${PWD} -w ${PWD} <container> -c " $@"
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