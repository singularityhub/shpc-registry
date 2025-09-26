---
layout: container
name:  "quay.io/biocontainers/bioframe"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioframe/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioframe/container.yaml"
updated_at: "2025-09-26 03:26:42.304902"
latest: "0.8.0--pyhdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioframe"
aliases:
 - "bam2pairs"
 - "column_remover.pl"
 - "duplicate_header_remover.pl"
 - "fragment_4dnpairs.pl"
 - "juicer_shortform2pairs.pl"
 - "merge-pairs.sh"
 - "merged_nodup2pairs.pl"
 - "old_merged_nodup2pairs.pl"
 - "pairix"
 - "pairs_merger"
versions:
 - "0.3.3--pyhdfd78af_0"
 - "0.4.0--pyhdfd78af_0"
 - "0.4.1--pyhdfd78af_0"
 - "0.5.0--pyhdfd78af_0"
 - "0.5.1--pyhdfd78af_0"
 - "0.6.1--pyhdfd78af_0"
 - "0.6.3--pyhdfd78af_0"
 - "0.6.4--pyhdfd78af_0"
 - "0.7.0--pyhdfd78af_0"
 - "0.7.2--pyhdfd78af_0"
 - "0.8.0--pyhdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioframe"
config: {"url": "https://biocontainers.pro/tools/bioframe", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioframe", "latest": {"0.8.0--pyhdfd78af_0": "sha256:a34a8602a473a96b6714194c62a93fa0710de9eed8c50c2bf3502c2d1d532326"}, "tags": {"0.3.3--pyhdfd78af_0": "sha256:d0d4f6e99abcbc4b5b94225ead9eb539b58749e58da0bf1387dbac36281355ab", "0.4.0--pyhdfd78af_0": "sha256:8a816ed8508812fd6757548f0d9daf6a9064f349e512c1b1274a08c25fcdb37e", "0.4.1--pyhdfd78af_0": "sha256:6053643e52baa1a18ec6e9ec6c56fba39da5642b7c6f69f58bf8c2aac04385b7", "0.5.0--pyhdfd78af_0": "sha256:041ee302276a32447289e47388198445dd5d4521c2dc4a1c278eaa6cffb22929", "0.5.1--pyhdfd78af_0": "sha256:a46612986cd567797b252b8078aa1c425857eb1af683f0b2dc85870d1a7aeafb", "0.6.1--pyhdfd78af_0": "sha256:2308209e994f1cfe7f147ee7845e726fde60466f6f95c77f4969b4963fbc8ad4", "0.6.3--pyhdfd78af_0": "sha256:bb662792e94b18ee2990a202bcf683b5e6e054c74fcacbaf9890c2881095cd8a", "0.6.4--pyhdfd78af_0": "sha256:a3c37d2762af64ad831b1528587f040fbb675ddbc425f7da9ea6e7051b9e73fd", "0.7.0--pyhdfd78af_0": "sha256:130488f93b559682bc5672cac8ab7e54542fd8a78b9e25c137cc1280b89f14c4", "0.7.2--pyhdfd78af_0": "sha256:ae5722c265c43523fee1d146c67da982742947aa964d385ec3d03059a356e0f8", "0.8.0--pyhdfd78af_0": "sha256:a34a8602a473a96b6714194c62a93fa0710de9eed8c50c2bf3502c2d1d532326"}, "docker": "quay.io/biocontainers/bioframe", "aliases": {"bam2pairs": "/usr/local/bin/bam2pairs", "column_remover.pl": "/usr/local/bin/column_remover.pl", "duplicate_header_remover.pl": "/usr/local/bin/duplicate_header_remover.pl", "fragment_4dnpairs.pl": "/usr/local/bin/fragment_4dnpairs.pl", "juicer_shortform2pairs.pl": "/usr/local/bin/juicer_shortform2pairs.pl", "merge-pairs.sh": "/usr/local/bin/merge-pairs.sh", "merged_nodup2pairs.pl": "/usr/local/bin/merged_nodup2pairs.pl", "old_merged_nodup2pairs.pl": "/usr/local/bin/old_merged_nodup2pairs.pl", "pairix": "/usr/local/bin/pairix", "pairs_merger": "/usr/local/bin/pairs_merger"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioframe.
shpc-registry automated BioContainers addition for bioframe
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioframe
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioframe:0.8.0--pyhdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioframe/0.8.0--pyhdfd78af_0
$ module help quay.io/biocontainers/bioframe/0.8.0--pyhdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioframe-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioframe-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioframe-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioframe-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioframe-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioframe-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### bam2pairs

```bash
$ singularity exec <container> /usr/local/bin/bam2pairs
$ podman run --it --rm --entrypoint /usr/local/bin/bam2pairs   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bam2pairs   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### column_remover.pl

```bash
$ singularity exec <container> /usr/local/bin/column_remover.pl
$ podman run --it --rm --entrypoint /usr/local/bin/column_remover.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/column_remover.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### duplicate_header_remover.pl

```bash
$ singularity exec <container> /usr/local/bin/duplicate_header_remover.pl
$ podman run --it --rm --entrypoint /usr/local/bin/duplicate_header_remover.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/duplicate_header_remover.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fragment_4dnpairs.pl

```bash
$ singularity exec <container> /usr/local/bin/fragment_4dnpairs.pl
$ podman run --it --rm --entrypoint /usr/local/bin/fragment_4dnpairs.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fragment_4dnpairs.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### juicer_shortform2pairs.pl

```bash
$ singularity exec <container> /usr/local/bin/juicer_shortform2pairs.pl
$ podman run --it --rm --entrypoint /usr/local/bin/juicer_shortform2pairs.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/juicer_shortform2pairs.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### merge-pairs.sh

```bash
$ singularity exec <container> /usr/local/bin/merge-pairs.sh
$ podman run --it --rm --entrypoint /usr/local/bin/merge-pairs.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/merge-pairs.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### merged_nodup2pairs.pl

```bash
$ singularity exec <container> /usr/local/bin/merged_nodup2pairs.pl
$ podman run --it --rm --entrypoint /usr/local/bin/merged_nodup2pairs.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/merged_nodup2pairs.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### old_merged_nodup2pairs.pl

```bash
$ singularity exec <container> /usr/local/bin/old_merged_nodup2pairs.pl
$ podman run --it --rm --entrypoint /usr/local/bin/old_merged_nodup2pairs.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/old_merged_nodup2pairs.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pairix

```bash
$ singularity exec <container> /usr/local/bin/pairix
$ podman run --it --rm --entrypoint /usr/local/bin/pairix   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pairix   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pairs_merger

```bash
$ singularity exec <container> /usr/local/bin/pairs_merger
$ podman run --it --rm --entrypoint /usr/local/bin/pairs_merger   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pairs_merger   -v ${PWD} -w ${PWD} <container> -c " $@"
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