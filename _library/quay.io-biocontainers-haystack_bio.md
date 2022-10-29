---
layout: container
name:  "quay.io/biocontainers/haystack_bio"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/haystack_bio/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/haystack_bio/container.yaml"
updated_at: "2022-10-29 05:43:57.312921"
latest: "v0.5.0--0"
container_url: "https://biocontainers.pro/tools/haystack_bio"
aliases:
 - "bigWigAverageOverBed"
 - "font2c"
 - "haystack_download_genome"
 - "haystack_hotspots"
 - "haystack_motifs"
 - "haystack_pipeline"
 - "haystack_run_test"
 - "haystack_tf_activity_plane"
 - "msql2mysql"
 - "mysql_convert_table_format"
 - "mysql_find_rows"
 - "mysql_fix_extensions"
 - "mysql_setpermission"
 - "mysql_waitpid"
 - "mysql_zap"
 - "mysqlaccess"
 - "mysqlaccess.conf"
 - "mysqlbug"
 - "mysqlhotcopy"
 - "wftopfa"
 - "ace2sam"
 - "aggregate_scores_in_intervals.py"
 - "align_print_template.py"
 - "alphtype"
 - "ama"
 - "ama-qvalues"
 - "ame"
 - "annotate.py"
 - "annotateBed"
 - "appletviewer"
versions:
 - "v0.5.0--0"
description: "shpc-registry automated BioContainers addition for haystack_bio"
config: {"url": "https://biocontainers.pro/tools/haystack_bio", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for haystack_bio", "latest": {"v0.5.0--0": "sha256:65b010177a7b945fef60ba38251f70d7e40402274982fd90310929fd62396ae3"}, "tags": {"v0.5.0--0": "sha256:65b010177a7b945fef60ba38251f70d7e40402274982fd90310929fd62396ae3"}, "docker": "quay.io/biocontainers/haystack_bio", "aliases": {"bigWigAverageOverBed": "/usr/local/bin/bigWigAverageOverBed", "font2c": "/usr/local/bin/font2c", "haystack_download_genome": "/usr/local/bin/haystack_download_genome", "haystack_hotspots": "/usr/local/bin/haystack_hotspots", "haystack_motifs": "/usr/local/bin/haystack_motifs", "haystack_pipeline": "/usr/local/bin/haystack_pipeline", "haystack_run_test": "/usr/local/bin/haystack_run_test", "haystack_tf_activity_plane": "/usr/local/bin/haystack_tf_activity_plane", "msql2mysql": "/usr/local/bin/msql2mysql", "mysql_convert_table_format": "/usr/local/bin/mysql_convert_table_format", "mysql_find_rows": "/usr/local/bin/mysql_find_rows", "mysql_fix_extensions": "/usr/local/bin/mysql_fix_extensions", "mysql_setpermission": "/usr/local/bin/mysql_setpermission", "mysql_waitpid": "/usr/local/bin/mysql_waitpid", "mysql_zap": "/usr/local/bin/mysql_zap", "mysqlaccess": "/usr/local/bin/mysqlaccess", "mysqlaccess.conf": "/usr/local/bin/mysqlaccess.conf", "mysqlbug": "/usr/local/bin/mysqlbug", "mysqlhotcopy": "/usr/local/bin/mysqlhotcopy", "wftopfa": "/usr/local/bin/wftopfa", "ace2sam": "/usr/local/bin/ace2sam", "aggregate_scores_in_intervals.py": "/usr/local/bin/aggregate_scores_in_intervals.py", "align_print_template.py": "/usr/local/bin/align_print_template.py", "alphtype": "/usr/local/bin/alphtype", "ama": "/usr/local/bin/ama", "ama-qvalues": "/usr/local/bin/ama-qvalues", "ame": "/usr/local/bin/ame", "annotate.py": "/usr/local/bin/annotate.py", "annotateBed": "/usr/local/bin/annotateBed", "appletviewer": "/usr/local/bin/appletviewer"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/haystack_bio.
shpc-registry automated BioContainers addition for haystack_bio
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/haystack_bio
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/haystack_bio:v0.5.0--0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/haystack_bio/v0.5.0--0
$ module help quay.io/biocontainers/haystack_bio/v0.5.0--0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### haystack_bio-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### haystack_bio-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### haystack_bio-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### haystack_bio-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### haystack_bio-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### haystack_bio-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### bigWigAverageOverBed

```bash
$ singularity exec <container> /usr/local/bin/bigWigAverageOverBed
$ podman run --it --rm --entrypoint /usr/local/bin/bigWigAverageOverBed   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bigWigAverageOverBed   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### font2c

```bash
$ singularity exec <container> /usr/local/bin/font2c
$ podman run --it --rm --entrypoint /usr/local/bin/font2c   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/font2c   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### haystack_download_genome

```bash
$ singularity exec <container> /usr/local/bin/haystack_download_genome
$ podman run --it --rm --entrypoint /usr/local/bin/haystack_download_genome   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/haystack_download_genome   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### haystack_hotspots

```bash
$ singularity exec <container> /usr/local/bin/haystack_hotspots
$ podman run --it --rm --entrypoint /usr/local/bin/haystack_hotspots   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/haystack_hotspots   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### haystack_motifs

```bash
$ singularity exec <container> /usr/local/bin/haystack_motifs
$ podman run --it --rm --entrypoint /usr/local/bin/haystack_motifs   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/haystack_motifs   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### haystack_pipeline

```bash
$ singularity exec <container> /usr/local/bin/haystack_pipeline
$ podman run --it --rm --entrypoint /usr/local/bin/haystack_pipeline   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/haystack_pipeline   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### haystack_run_test

```bash
$ singularity exec <container> /usr/local/bin/haystack_run_test
$ podman run --it --rm --entrypoint /usr/local/bin/haystack_run_test   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/haystack_run_test   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### haystack_tf_activity_plane

```bash
$ singularity exec <container> /usr/local/bin/haystack_tf_activity_plane
$ podman run --it --rm --entrypoint /usr/local/bin/haystack_tf_activity_plane   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/haystack_tf_activity_plane   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### msql2mysql

```bash
$ singularity exec <container> /usr/local/bin/msql2mysql
$ podman run --it --rm --entrypoint /usr/local/bin/msql2mysql   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/msql2mysql   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mysql_convert_table_format

```bash
$ singularity exec <container> /usr/local/bin/mysql_convert_table_format
$ podman run --it --rm --entrypoint /usr/local/bin/mysql_convert_table_format   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mysql_convert_table_format   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mysql_find_rows

```bash
$ singularity exec <container> /usr/local/bin/mysql_find_rows
$ podman run --it --rm --entrypoint /usr/local/bin/mysql_find_rows   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mysql_find_rows   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mysql_fix_extensions

```bash
$ singularity exec <container> /usr/local/bin/mysql_fix_extensions
$ podman run --it --rm --entrypoint /usr/local/bin/mysql_fix_extensions   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mysql_fix_extensions   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mysql_setpermission

```bash
$ singularity exec <container> /usr/local/bin/mysql_setpermission
$ podman run --it --rm --entrypoint /usr/local/bin/mysql_setpermission   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mysql_setpermission   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mysql_waitpid

```bash
$ singularity exec <container> /usr/local/bin/mysql_waitpid
$ podman run --it --rm --entrypoint /usr/local/bin/mysql_waitpid   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mysql_waitpid   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mysql_zap

```bash
$ singularity exec <container> /usr/local/bin/mysql_zap
$ podman run --it --rm --entrypoint /usr/local/bin/mysql_zap   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mysql_zap   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mysqlaccess

```bash
$ singularity exec <container> /usr/local/bin/mysqlaccess
$ podman run --it --rm --entrypoint /usr/local/bin/mysqlaccess   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mysqlaccess   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mysqlaccess.conf

```bash
$ singularity exec <container> /usr/local/bin/mysqlaccess.conf
$ podman run --it --rm --entrypoint /usr/local/bin/mysqlaccess.conf   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mysqlaccess.conf   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mysqlbug

```bash
$ singularity exec <container> /usr/local/bin/mysqlbug
$ podman run --it --rm --entrypoint /usr/local/bin/mysqlbug   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mysqlbug   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mysqlhotcopy

```bash
$ singularity exec <container> /usr/local/bin/mysqlhotcopy
$ podman run --it --rm --entrypoint /usr/local/bin/mysqlhotcopy   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mysqlhotcopy   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### wftopfa

```bash
$ singularity exec <container> /usr/local/bin/wftopfa
$ podman run --it --rm --entrypoint /usr/local/bin/wftopfa   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/wftopfa   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ace2sam

```bash
$ singularity exec <container> /usr/local/bin/ace2sam
$ podman run --it --rm --entrypoint /usr/local/bin/ace2sam   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ace2sam   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### aggregate_scores_in_intervals.py

```bash
$ singularity exec <container> /usr/local/bin/aggregate_scores_in_intervals.py
$ podman run --it --rm --entrypoint /usr/local/bin/aggregate_scores_in_intervals.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/aggregate_scores_in_intervals.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### align_print_template.py

```bash
$ singularity exec <container> /usr/local/bin/align_print_template.py
$ podman run --it --rm --entrypoint /usr/local/bin/align_print_template.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/align_print_template.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### alphtype

```bash
$ singularity exec <container> /usr/local/bin/alphtype
$ podman run --it --rm --entrypoint /usr/local/bin/alphtype   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/alphtype   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ama

```bash
$ singularity exec <container> /usr/local/bin/ama
$ podman run --it --rm --entrypoint /usr/local/bin/ama   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ama   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ama-qvalues

```bash
$ singularity exec <container> /usr/local/bin/ama-qvalues
$ podman run --it --rm --entrypoint /usr/local/bin/ama-qvalues   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ama-qvalues   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ame

```bash
$ singularity exec <container> /usr/local/bin/ame
$ podman run --it --rm --entrypoint /usr/local/bin/ame   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ame   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### annotate.py

```bash
$ singularity exec <container> /usr/local/bin/annotate.py
$ podman run --it --rm --entrypoint /usr/local/bin/annotate.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/annotate.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### annotateBed

```bash
$ singularity exec <container> /usr/local/bin/annotateBed
$ podman run --it --rm --entrypoint /usr/local/bin/annotateBed   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/annotateBed   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### appletviewer

```bash
$ singularity exec <container> /usr/local/bin/appletviewer
$ podman run --it --rm --entrypoint /usr/local/bin/appletviewer   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/appletviewer   -v ${PWD} -w ${PWD} <container> -c " $@"
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