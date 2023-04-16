---
layout: container
name:  "quay.io/biocontainers/batvi"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/batvi/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/batvi/container.yaml"
updated_at: "2023-04-16 02:41:53.561063"
latest: "1.04--h5b5514e_7"
container_url: "https://biocontainers.pro/tools/batvi"
aliases:
 - "call_integrations.sh"
 - "cat_sorted_sam.sh"
 - "clean_run.sh"
 - "collate.sh"
 - "collate_from_file.sh"
 - "combine_hits.pl"
 - "commandline.sh"
 - "convert_to_fastq.sh"
 - "email.sh"
 - "extract_hbv_from_fasta.sh"
 - "extract_sam_xargs.sh"
 - "extract_unmapped_and_oneside.sh"
 - "extracthbv.sh"
 - "gen_paths.sh"
 - "get_blast_hits.sh"
 - "get_reads.pl"
 - "hbvblast.sh"
 - "join_sam.sh"
 - "manualcompile.sh"
 - "relabelunbugreads.sh"
 - "search_text.sh"
 - "sort_by_name.sh"
 - "unbug.pl"
 - "unbug.sh"
 - "unbug_xarg.sh"
 - "view_xargs.sh"
 - "build.sh"
 - "picard"
 - "edirect.py"
 - "filter-columns"
 - "fuse-segments"
 - "gene2range"
 - "tbl2prod"
 - "uniq-table"
 - "align-columns"
 - "blst2tkns"
versions:
 - "1.04--h5b5514e_7"
description: "shpc-registry automated BioContainers addition for batvi"
config: {"url": "https://biocontainers.pro/tools/batvi", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for batvi", "latest": {"1.04--h5b5514e_7": "sha256:468cc76c6d0cae8151e58a7ff9bc7a274a0c0624f437959a4f4343fbb1b06cb6"}, "tags": {"1.04--h5b5514e_7": "sha256:468cc76c6d0cae8151e58a7ff9bc7a274a0c0624f437959a4f4343fbb1b06cb6"}, "docker": "quay.io/biocontainers/batvi", "aliases": {"call_integrations.sh": "/usr/local/bin/call_integrations.sh", "cat_sorted_sam.sh": "/usr/local/bin/cat_sorted_sam.sh", "clean_run.sh": "/usr/local/bin/clean_run.sh", "collate.sh": "/usr/local/bin/collate.sh", "collate_from_file.sh": "/usr/local/bin/collate_from_file.sh", "combine_hits.pl": "/usr/local/bin/combine_hits.pl", "commandline.sh": "/usr/local/bin/commandline.sh", "convert_to_fastq.sh": "/usr/local/bin/convert_to_fastq.sh", "email.sh": "/usr/local/bin/email.sh", "extract_hbv_from_fasta.sh": "/usr/local/bin/extract_hbv_from_fasta.sh", "extract_sam_xargs.sh": "/usr/local/bin/extract_sam_xargs.sh", "extract_unmapped_and_oneside.sh": "/usr/local/bin/extract_unmapped_and_oneside.sh", "extracthbv.sh": "/usr/local/bin/extracthbv.sh", "gen_paths.sh": "/usr/local/bin/gen_paths.sh", "get_blast_hits.sh": "/usr/local/bin/get_blast_hits.sh", "get_reads.pl": "/usr/local/bin/get_reads.pl", "hbvblast.sh": "/usr/local/bin/hbvblast.sh", "join_sam.sh": "/usr/local/bin/join_sam.sh", "manualcompile.sh": "/usr/local/bin/manualcompile.sh", "relabelunbugreads.sh": "/usr/local/bin/relabelunbugreads.sh", "search_text.sh": "/usr/local/bin/search_text.sh", "sort_by_name.sh": "/usr/local/bin/sort_by_name.sh", "unbug.pl": "/usr/local/bin/unbug.pl", "unbug.sh": "/usr/local/bin/unbug.sh", "unbug_xarg.sh": "/usr/local/bin/unbug_xarg.sh", "view_xargs.sh": "/usr/local/bin/view_xargs.sh", "build.sh": "/usr/local/bin/build.sh", "picard": "/usr/local/bin/picard", "edirect.py": "/usr/local/bin/edirect.py", "filter-columns": "/usr/local/bin/filter-columns", "fuse-segments": "/usr/local/bin/fuse-segments", "gene2range": "/usr/local/bin/gene2range", "tbl2prod": "/usr/local/bin/tbl2prod", "uniq-table": "/usr/local/bin/uniq-table", "align-columns": "/usr/local/bin/align-columns", "blst2tkns": "/usr/local/bin/blst2tkns"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/batvi.
shpc-registry automated BioContainers addition for batvi
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/batvi
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/batvi:1.04--h5b5514e_7
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/batvi/1.04--h5b5514e_7
$ module help quay.io/biocontainers/batvi/1.04--h5b5514e_7
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### batvi-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### batvi-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### batvi-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### batvi-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### batvi-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### batvi-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### call_integrations.sh

```bash
$ singularity exec <container> /usr/local/bin/call_integrations.sh
$ podman run --it --rm --entrypoint /usr/local/bin/call_integrations.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/call_integrations.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### cat_sorted_sam.sh

```bash
$ singularity exec <container> /usr/local/bin/cat_sorted_sam.sh
$ podman run --it --rm --entrypoint /usr/local/bin/cat_sorted_sam.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cat_sorted_sam.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### clean_run.sh

```bash
$ singularity exec <container> /usr/local/bin/clean_run.sh
$ podman run --it --rm --entrypoint /usr/local/bin/clean_run.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/clean_run.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### collate.sh

```bash
$ singularity exec <container> /usr/local/bin/collate.sh
$ podman run --it --rm --entrypoint /usr/local/bin/collate.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/collate.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### collate_from_file.sh

```bash
$ singularity exec <container> /usr/local/bin/collate_from_file.sh
$ podman run --it --rm --entrypoint /usr/local/bin/collate_from_file.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/collate_from_file.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### combine_hits.pl

```bash
$ singularity exec <container> /usr/local/bin/combine_hits.pl
$ podman run --it --rm --entrypoint /usr/local/bin/combine_hits.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/combine_hits.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### commandline.sh

```bash
$ singularity exec <container> /usr/local/bin/commandline.sh
$ podman run --it --rm --entrypoint /usr/local/bin/commandline.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/commandline.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### convert_to_fastq.sh

```bash
$ singularity exec <container> /usr/local/bin/convert_to_fastq.sh
$ podman run --it --rm --entrypoint /usr/local/bin/convert_to_fastq.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/convert_to_fastq.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### email.sh

```bash
$ singularity exec <container> /usr/local/bin/email.sh
$ podman run --it --rm --entrypoint /usr/local/bin/email.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/email.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### extract_hbv_from_fasta.sh

```bash
$ singularity exec <container> /usr/local/bin/extract_hbv_from_fasta.sh
$ podman run --it --rm --entrypoint /usr/local/bin/extract_hbv_from_fasta.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/extract_hbv_from_fasta.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### extract_sam_xargs.sh

```bash
$ singularity exec <container> /usr/local/bin/extract_sam_xargs.sh
$ podman run --it --rm --entrypoint /usr/local/bin/extract_sam_xargs.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/extract_sam_xargs.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### extract_unmapped_and_oneside.sh

```bash
$ singularity exec <container> /usr/local/bin/extract_unmapped_and_oneside.sh
$ podman run --it --rm --entrypoint /usr/local/bin/extract_unmapped_and_oneside.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/extract_unmapped_and_oneside.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### extracthbv.sh

```bash
$ singularity exec <container> /usr/local/bin/extracthbv.sh
$ podman run --it --rm --entrypoint /usr/local/bin/extracthbv.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/extracthbv.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gen_paths.sh

```bash
$ singularity exec <container> /usr/local/bin/gen_paths.sh
$ podman run --it --rm --entrypoint /usr/local/bin/gen_paths.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gen_paths.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### get_blast_hits.sh

```bash
$ singularity exec <container> /usr/local/bin/get_blast_hits.sh
$ podman run --it --rm --entrypoint /usr/local/bin/get_blast_hits.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/get_blast_hits.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### get_reads.pl

```bash
$ singularity exec <container> /usr/local/bin/get_reads.pl
$ podman run --it --rm --entrypoint /usr/local/bin/get_reads.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/get_reads.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### hbvblast.sh

```bash
$ singularity exec <container> /usr/local/bin/hbvblast.sh
$ podman run --it --rm --entrypoint /usr/local/bin/hbvblast.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/hbvblast.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### join_sam.sh

```bash
$ singularity exec <container> /usr/local/bin/join_sam.sh
$ podman run --it --rm --entrypoint /usr/local/bin/join_sam.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/join_sam.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### manualcompile.sh

```bash
$ singularity exec <container> /usr/local/bin/manualcompile.sh
$ podman run --it --rm --entrypoint /usr/local/bin/manualcompile.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/manualcompile.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### relabelunbugreads.sh

```bash
$ singularity exec <container> /usr/local/bin/relabelunbugreads.sh
$ podman run --it --rm --entrypoint /usr/local/bin/relabelunbugreads.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/relabelunbugreads.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### search_text.sh

```bash
$ singularity exec <container> /usr/local/bin/search_text.sh
$ podman run --it --rm --entrypoint /usr/local/bin/search_text.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/search_text.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### sort_by_name.sh

```bash
$ singularity exec <container> /usr/local/bin/sort_by_name.sh
$ podman run --it --rm --entrypoint /usr/local/bin/sort_by_name.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/sort_by_name.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### unbug.pl

```bash
$ singularity exec <container> /usr/local/bin/unbug.pl
$ podman run --it --rm --entrypoint /usr/local/bin/unbug.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/unbug.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### unbug.sh

```bash
$ singularity exec <container> /usr/local/bin/unbug.sh
$ podman run --it --rm --entrypoint /usr/local/bin/unbug.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/unbug.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### unbug_xarg.sh

```bash
$ singularity exec <container> /usr/local/bin/unbug_xarg.sh
$ podman run --it --rm --entrypoint /usr/local/bin/unbug_xarg.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/unbug_xarg.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### view_xargs.sh

```bash
$ singularity exec <container> /usr/local/bin/view_xargs.sh
$ podman run --it --rm --entrypoint /usr/local/bin/view_xargs.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/view_xargs.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### build.sh

```bash
$ singularity exec <container> /usr/local/bin/build.sh
$ podman run --it --rm --entrypoint /usr/local/bin/build.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/build.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### picard

```bash
$ singularity exec <container> /usr/local/bin/picard
$ podman run --it --rm --entrypoint /usr/local/bin/picard   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/picard   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### edirect.py

```bash
$ singularity exec <container> /usr/local/bin/edirect.py
$ podman run --it --rm --entrypoint /usr/local/bin/edirect.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/edirect.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### filter-columns

```bash
$ singularity exec <container> /usr/local/bin/filter-columns
$ podman run --it --rm --entrypoint /usr/local/bin/filter-columns   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/filter-columns   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fuse-segments

```bash
$ singularity exec <container> /usr/local/bin/fuse-segments
$ podman run --it --rm --entrypoint /usr/local/bin/fuse-segments   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fuse-segments   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gene2range

```bash
$ singularity exec <container> /usr/local/bin/gene2range
$ podman run --it --rm --entrypoint /usr/local/bin/gene2range   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gene2range   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### tbl2prod

```bash
$ singularity exec <container> /usr/local/bin/tbl2prod
$ podman run --it --rm --entrypoint /usr/local/bin/tbl2prod   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/tbl2prod   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### uniq-table

```bash
$ singularity exec <container> /usr/local/bin/uniq-table
$ podman run --it --rm --entrypoint /usr/local/bin/uniq-table   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/uniq-table   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### align-columns

```bash
$ singularity exec <container> /usr/local/bin/align-columns
$ podman run --it --rm --entrypoint /usr/local/bin/align-columns   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/align-columns   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### blst2tkns

```bash
$ singularity exec <container> /usr/local/bin/blst2tkns
$ podman run --it --rm --entrypoint /usr/local/bin/blst2tkns   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/blst2tkns   -v ${PWD} -w ${PWD} <container> -c " $@"
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