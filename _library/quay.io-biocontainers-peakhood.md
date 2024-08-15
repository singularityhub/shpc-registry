---
layout: container
name:  "quay.io/biocontainers/peakhood"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/peakhood/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/peakhood/container.yaml"
updated_at: "2024-08-15 03:13:11.203579"
latest: "0.3--pyhdfd78af_0"
container_url: "https://biocontainers.pro/tools/peakhood"
aliases:
 - "bed_generate_unique_ids.py"
 - "gtf_add_transcript_biotype_info.py"
 - "peakhood"
 - "twoBitToFa"
 - "twoBitInfo"
 - "markdown_py"
 - "my_print_defaults"
 - "mysql_config"
 - "perror"
 - "fasta-sanitize.pl"
 - "shiftBed"
 - "plot-ampliconstats"
 - "annotateBed"
versions:
 - "0.3--pyhdfd78af_0"
description: "shpc-registry automated BioContainers addition for peakhood"
config: {"url": "https://biocontainers.pro/tools/peakhood", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for peakhood", "latest": {"0.3--pyhdfd78af_0": "sha256:316fc54775265c367fb0d8d1d7314860743da2b511f9b8438a1f3994af8c0535"}, "tags": {"0.3--pyhdfd78af_0": "sha256:316fc54775265c367fb0d8d1d7314860743da2b511f9b8438a1f3994af8c0535"}, "docker": "quay.io/biocontainers/peakhood", "aliases": {"bed_generate_unique_ids.py": "/usr/local/bin/bed_generate_unique_ids.py", "gtf_add_transcript_biotype_info.py": "/usr/local/bin/gtf_add_transcript_biotype_info.py", "peakhood": "/usr/local/bin/peakhood", "twoBitToFa": "/usr/local/bin/twoBitToFa", "twoBitInfo": "/usr/local/bin/twoBitInfo", "markdown_py": "/usr/local/bin/markdown_py", "my_print_defaults": "/usr/local/bin/my_print_defaults", "mysql_config": "/usr/local/bin/mysql_config", "perror": "/usr/local/bin/perror", "fasta-sanitize.pl": "/usr/local/bin/fasta-sanitize.pl", "shiftBed": "/usr/local/bin/shiftBed", "plot-ampliconstats": "/usr/local/bin/plot-ampliconstats", "annotateBed": "/usr/local/bin/annotateBed"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/peakhood.
shpc-registry automated BioContainers addition for peakhood
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/peakhood
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/peakhood:0.3--pyhdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/peakhood/0.3--pyhdfd78af_0
$ module help quay.io/biocontainers/peakhood/0.3--pyhdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### peakhood-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### peakhood-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### peakhood-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### peakhood-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### peakhood-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### peakhood-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### bed_generate_unique_ids.py

```bash
$ singularity exec <container> /usr/local/bin/bed_generate_unique_ids.py
$ podman run --it --rm --entrypoint /usr/local/bin/bed_generate_unique_ids.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bed_generate_unique_ids.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gtf_add_transcript_biotype_info.py

```bash
$ singularity exec <container> /usr/local/bin/gtf_add_transcript_biotype_info.py
$ podman run --it --rm --entrypoint /usr/local/bin/gtf_add_transcript_biotype_info.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gtf_add_transcript_biotype_info.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### peakhood

```bash
$ singularity exec <container> /usr/local/bin/peakhood
$ podman run --it --rm --entrypoint /usr/local/bin/peakhood   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/peakhood   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### twoBitToFa

```bash
$ singularity exec <container> /usr/local/bin/twoBitToFa
$ podman run --it --rm --entrypoint /usr/local/bin/twoBitToFa   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/twoBitToFa   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### twoBitInfo

```bash
$ singularity exec <container> /usr/local/bin/twoBitInfo
$ podman run --it --rm --entrypoint /usr/local/bin/twoBitInfo   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/twoBitInfo   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### markdown_py

```bash
$ singularity exec <container> /usr/local/bin/markdown_py
$ podman run --it --rm --entrypoint /usr/local/bin/markdown_py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/markdown_py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### my_print_defaults

```bash
$ singularity exec <container> /usr/local/bin/my_print_defaults
$ podman run --it --rm --entrypoint /usr/local/bin/my_print_defaults   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/my_print_defaults   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mysql_config

```bash
$ singularity exec <container> /usr/local/bin/mysql_config
$ podman run --it --rm --entrypoint /usr/local/bin/mysql_config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mysql_config   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### perror

```bash
$ singularity exec <container> /usr/local/bin/perror
$ podman run --it --rm --entrypoint /usr/local/bin/perror   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/perror   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fasta-sanitize.pl

```bash
$ singularity exec <container> /usr/local/bin/fasta-sanitize.pl
$ podman run --it --rm --entrypoint /usr/local/bin/fasta-sanitize.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fasta-sanitize.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### shiftBed

```bash
$ singularity exec <container> /usr/local/bin/shiftBed
$ podman run --it --rm --entrypoint /usr/local/bin/shiftBed   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/shiftBed   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### plot-ampliconstats

```bash
$ singularity exec <container> /usr/local/bin/plot-ampliconstats
$ podman run --it --rm --entrypoint /usr/local/bin/plot-ampliconstats   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/plot-ampliconstats   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### annotateBed

```bash
$ singularity exec <container> /usr/local/bin/annotateBed
$ podman run --it --rm --entrypoint /usr/local/bin/annotateBed   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/annotateBed   -v ${PWD} -w ${PWD} <container> -c " $@"
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