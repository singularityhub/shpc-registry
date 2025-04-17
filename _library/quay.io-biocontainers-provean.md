---
layout: container
name:  "quay.io/biocontainers/provean"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/provean/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/provean/container.yaml"
updated_at: "2025-04-17 03:10:14.134521"
latest: "1.1.5--h503566f_3"
container_url: "https://biocontainers.pro/tools/provean"
aliases:
 - "provean"
 - "provean.sh"
 - "FET.pl"
 - "cd-hit-clstr_2_blm8.pl"
 - "clstr_list.pl"
 - "clstr_list_sort.pl"
 - "cd-hit"
 - "cd-hit-2d"
 - "cd-hit-2d-para.pl"
 - "cd-hit-454"
 - "cd-hit-div"
 - "cd-hit-div.pl"
 - "cd-hit-est-2d"
 - "cd-hit-para.pl"
 - "clstr2tree.pl"
 - "clstr2txt.pl"
 - "clstr2xml.pl"
 - "clstr_cut.pl"
 - "clstr_merge.pl"
 - "clstr_merge_noorder.pl"
 - "clstr_quality_eval.pl"
 - "clstr_quality_eval_by_link.pl"
 - "clstr_reduce.pl"
 - "clstr_renumber.pl"
 - "clstr_rep.pl"
 - "clstr_reps_faa_rev.pl"
 - "clstr_rev.pl"
versions:
 - "1.1.5--h87f3376_1"
 - "1.1.5--hdbdd923_2"
 - "1.1.5--h503566f_3"
description: "singularity registry hpc automated addition for provean"
config: {"url": "https://biocontainers.pro/tools/provean", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for provean", "latest": {"1.1.5--h503566f_3": "sha256:e41d06ff0c642c368b827beef4db3ce95f6f515534b83a4fe3664b2a737a65e9"}, "tags": {"1.1.5--h87f3376_1": "sha256:e3e21b1e0949c6ce71ca91ea86a92e3c51b89c79cbfde6d8388587b7b54c3dc7", "1.1.5--hdbdd923_2": "sha256:93aa495a461ddf9f261e8873e53635490937a9c7d09c0b646b92ff4061a41c26", "1.1.5--h503566f_3": "sha256:e41d06ff0c642c368b827beef4db3ce95f6f515534b83a4fe3664b2a737a65e9"}, "docker": "quay.io/biocontainers/provean", "aliases": {"provean": "/usr/local/bin/provean", "provean.sh": "/usr/local/bin/provean.sh", "FET.pl": "/usr/local/bin/FET.pl", "cd-hit-clstr_2_blm8.pl": "/usr/local/bin/cd-hit-clstr_2_blm8.pl", "clstr_list.pl": "/usr/local/bin/clstr_list.pl", "clstr_list_sort.pl": "/usr/local/bin/clstr_list_sort.pl", "cd-hit": "/usr/local/bin/cd-hit", "cd-hit-2d": "/usr/local/bin/cd-hit-2d", "cd-hit-2d-para.pl": "/usr/local/bin/cd-hit-2d-para.pl", "cd-hit-454": "/usr/local/bin/cd-hit-454", "cd-hit-div": "/usr/local/bin/cd-hit-div", "cd-hit-div.pl": "/usr/local/bin/cd-hit-div.pl", "cd-hit-est-2d": "/usr/local/bin/cd-hit-est-2d", "cd-hit-para.pl": "/usr/local/bin/cd-hit-para.pl", "clstr2tree.pl": "/usr/local/bin/clstr2tree.pl", "clstr2txt.pl": "/usr/local/bin/clstr2txt.pl", "clstr2xml.pl": "/usr/local/bin/clstr2xml.pl", "clstr_cut.pl": "/usr/local/bin/clstr_cut.pl", "clstr_merge.pl": "/usr/local/bin/clstr_merge.pl", "clstr_merge_noorder.pl": "/usr/local/bin/clstr_merge_noorder.pl", "clstr_quality_eval.pl": "/usr/local/bin/clstr_quality_eval.pl", "clstr_quality_eval_by_link.pl": "/usr/local/bin/clstr_quality_eval_by_link.pl", "clstr_reduce.pl": "/usr/local/bin/clstr_reduce.pl", "clstr_renumber.pl": "/usr/local/bin/clstr_renumber.pl", "clstr_rep.pl": "/usr/local/bin/clstr_rep.pl", "clstr_reps_faa_rev.pl": "/usr/local/bin/clstr_reps_faa_rev.pl", "clstr_rev.pl": "/usr/local/bin/clstr_rev.pl"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/provean.
singularity registry hpc automated addition for provean
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/provean
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/provean:1.1.5--h503566f_3
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/provean/1.1.5--h503566f_3
$ module help quay.io/biocontainers/provean/1.1.5--h503566f_3
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### provean-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### provean-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### provean-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### provean-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### provean-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### provean-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### provean

```bash
$ singularity exec <container> /usr/local/bin/provean
$ podman run --it --rm --entrypoint /usr/local/bin/provean   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/provean   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### provean.sh

```bash
$ singularity exec <container> /usr/local/bin/provean.sh
$ podman run --it --rm --entrypoint /usr/local/bin/provean.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/provean.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### FET.pl

```bash
$ singularity exec <container> /usr/local/bin/FET.pl
$ podman run --it --rm --entrypoint /usr/local/bin/FET.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/FET.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### cd-hit-clstr_2_blm8.pl

```bash
$ singularity exec <container> /usr/local/bin/cd-hit-clstr_2_blm8.pl
$ podman run --it --rm --entrypoint /usr/local/bin/cd-hit-clstr_2_blm8.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cd-hit-clstr_2_blm8.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### clstr_list.pl

```bash
$ singularity exec <container> /usr/local/bin/clstr_list.pl
$ podman run --it --rm --entrypoint /usr/local/bin/clstr_list.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/clstr_list.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### clstr_list_sort.pl

```bash
$ singularity exec <container> /usr/local/bin/clstr_list_sort.pl
$ podman run --it --rm --entrypoint /usr/local/bin/clstr_list_sort.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/clstr_list_sort.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### cd-hit

```bash
$ singularity exec <container> /usr/local/bin/cd-hit
$ podman run --it --rm --entrypoint /usr/local/bin/cd-hit   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cd-hit   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### cd-hit-2d

```bash
$ singularity exec <container> /usr/local/bin/cd-hit-2d
$ podman run --it --rm --entrypoint /usr/local/bin/cd-hit-2d   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cd-hit-2d   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### cd-hit-2d-para.pl

```bash
$ singularity exec <container> /usr/local/bin/cd-hit-2d-para.pl
$ podman run --it --rm --entrypoint /usr/local/bin/cd-hit-2d-para.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cd-hit-2d-para.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### cd-hit-454

```bash
$ singularity exec <container> /usr/local/bin/cd-hit-454
$ podman run --it --rm --entrypoint /usr/local/bin/cd-hit-454   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cd-hit-454   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### cd-hit-div

```bash
$ singularity exec <container> /usr/local/bin/cd-hit-div
$ podman run --it --rm --entrypoint /usr/local/bin/cd-hit-div   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cd-hit-div   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### cd-hit-div.pl

```bash
$ singularity exec <container> /usr/local/bin/cd-hit-div.pl
$ podman run --it --rm --entrypoint /usr/local/bin/cd-hit-div.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cd-hit-div.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### cd-hit-est-2d

```bash
$ singularity exec <container> /usr/local/bin/cd-hit-est-2d
$ podman run --it --rm --entrypoint /usr/local/bin/cd-hit-est-2d   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cd-hit-est-2d   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### cd-hit-para.pl

```bash
$ singularity exec <container> /usr/local/bin/cd-hit-para.pl
$ podman run --it --rm --entrypoint /usr/local/bin/cd-hit-para.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cd-hit-para.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### clstr2tree.pl

```bash
$ singularity exec <container> /usr/local/bin/clstr2tree.pl
$ podman run --it --rm --entrypoint /usr/local/bin/clstr2tree.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/clstr2tree.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### clstr2txt.pl

```bash
$ singularity exec <container> /usr/local/bin/clstr2txt.pl
$ podman run --it --rm --entrypoint /usr/local/bin/clstr2txt.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/clstr2txt.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### clstr2xml.pl

```bash
$ singularity exec <container> /usr/local/bin/clstr2xml.pl
$ podman run --it --rm --entrypoint /usr/local/bin/clstr2xml.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/clstr2xml.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### clstr_cut.pl

```bash
$ singularity exec <container> /usr/local/bin/clstr_cut.pl
$ podman run --it --rm --entrypoint /usr/local/bin/clstr_cut.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/clstr_cut.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### clstr_merge.pl

```bash
$ singularity exec <container> /usr/local/bin/clstr_merge.pl
$ podman run --it --rm --entrypoint /usr/local/bin/clstr_merge.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/clstr_merge.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### clstr_merge_noorder.pl

```bash
$ singularity exec <container> /usr/local/bin/clstr_merge_noorder.pl
$ podman run --it --rm --entrypoint /usr/local/bin/clstr_merge_noorder.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/clstr_merge_noorder.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### clstr_quality_eval.pl

```bash
$ singularity exec <container> /usr/local/bin/clstr_quality_eval.pl
$ podman run --it --rm --entrypoint /usr/local/bin/clstr_quality_eval.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/clstr_quality_eval.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### clstr_quality_eval_by_link.pl

```bash
$ singularity exec <container> /usr/local/bin/clstr_quality_eval_by_link.pl
$ podman run --it --rm --entrypoint /usr/local/bin/clstr_quality_eval_by_link.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/clstr_quality_eval_by_link.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### clstr_reduce.pl

```bash
$ singularity exec <container> /usr/local/bin/clstr_reduce.pl
$ podman run --it --rm --entrypoint /usr/local/bin/clstr_reduce.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/clstr_reduce.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### clstr_renumber.pl

```bash
$ singularity exec <container> /usr/local/bin/clstr_renumber.pl
$ podman run --it --rm --entrypoint /usr/local/bin/clstr_renumber.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/clstr_renumber.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### clstr_rep.pl

```bash
$ singularity exec <container> /usr/local/bin/clstr_rep.pl
$ podman run --it --rm --entrypoint /usr/local/bin/clstr_rep.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/clstr_rep.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### clstr_reps_faa_rev.pl

```bash
$ singularity exec <container> /usr/local/bin/clstr_reps_faa_rev.pl
$ podman run --it --rm --entrypoint /usr/local/bin/clstr_reps_faa_rev.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/clstr_reps_faa_rev.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### clstr_rev.pl

```bash
$ singularity exec <container> /usr/local/bin/clstr_rev.pl
$ podman run --it --rm --entrypoint /usr/local/bin/clstr_rev.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/clstr_rev.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
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