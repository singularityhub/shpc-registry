---
layout: container
name:  "quay.io/biocontainers/debreak"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/debreak/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/debreak/container.yaml"
updated_at: "2023-06-05 02:52:56.207050"
latest: "1.3--h9ee0642_0"
container_url: "https://biocontainers.pro/tools/debreak"
aliases:
 - "bsalign"
 - "complexsv.py"
 - "debreak"
 - "debreak_allpoa.py"
 - "debreak_detect.py"
 - "debreak_genotype.py"
 - "debreak_merge.py"
 - "debreak_merge_cluster.py"
 - "debreak_merge_contig.py"
 - "debreak_rescuedupfromins.py"
 - "debreak_rescuelargeins.py"
 - "debreak_resdup_selfalignment.py"
 - "debreak_writevcf.py"
 - "genefusion.py"
 - "wtdbg-cns"
 - "wtdbg2"
 - "wtpoa-cns"
 - "paftools.js"
 - "minimap2"
 - "ace2sam"
 - "blast2sam.pl"
 - "bowtie2sam.pl"
 - "export2sam.pl"
 - "interpolate_sam.pl"
 - "maq2sam-long"
 - "maq2sam-short"
 - "md5fa"
 - "md5sum-lite"
 - "plot-bamstats"
 - "psl2sam.pl"
 - "sam2vcf.pl"
 - "samtools.pl"
 - "seq_cache_populate.pl"
 - "soap2sam.pl"
 - "zoom2sam.pl"
 - "novo2sam.pl"
 - "wgsim"
 - "wgsim_eval.pl"
 - "samtools"
 - "htsfile"
 - "bgzip"
 - "tabix"
versions:
 - "1.3--h9ee0642_0"
description: "singularity registry hpc automated addition for debreak"
config: {"url": "https://biocontainers.pro/tools/debreak", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for debreak", "latest": {"1.3--h9ee0642_0": "sha256:e69aa709ef5f029361cca4cb4ef087753b71e3a63b0a7f5e8ea1ea7d0721fac6"}, "tags": {"1.3--h9ee0642_0": "sha256:e69aa709ef5f029361cca4cb4ef087753b71e3a63b0a7f5e8ea1ea7d0721fac6"}, "docker": "quay.io/biocontainers/debreak", "aliases": {"bsalign": "/usr/local/bin/bsalign", "complexsv.py": "/usr/local/bin/complexsv.py", "debreak": "/usr/local/bin/debreak", "debreak_allpoa.py": "/usr/local/bin/debreak_allpoa.py", "debreak_detect.py": "/usr/local/bin/debreak_detect.py", "debreak_genotype.py": "/usr/local/bin/debreak_genotype.py", "debreak_merge.py": "/usr/local/bin/debreak_merge.py", "debreak_merge_cluster.py": "/usr/local/bin/debreak_merge_cluster.py", "debreak_merge_contig.py": "/usr/local/bin/debreak_merge_contig.py", "debreak_rescuedupfromins.py": "/usr/local/bin/debreak_rescuedupfromins.py", "debreak_rescuelargeins.py": "/usr/local/bin/debreak_rescuelargeins.py", "debreak_resdup_selfalignment.py": "/usr/local/bin/debreak_resdup_selfalignment.py", "debreak_writevcf.py": "/usr/local/bin/debreak_writevcf.py", "genefusion.py": "/usr/local/bin/genefusion.py", "wtdbg-cns": "/usr/local/bin/wtdbg-cns", "wtdbg2": "/usr/local/bin/wtdbg2", "wtpoa-cns": "/usr/local/bin/wtpoa-cns", "paftools.js": "/usr/local/bin/paftools.js", "minimap2": "/usr/local/bin/minimap2", "ace2sam": "/usr/local/bin/ace2sam", "blast2sam.pl": "/usr/local/bin/blast2sam.pl", "bowtie2sam.pl": "/usr/local/bin/bowtie2sam.pl", "export2sam.pl": "/usr/local/bin/export2sam.pl", "interpolate_sam.pl": "/usr/local/bin/interpolate_sam.pl", "maq2sam-long": "/usr/local/bin/maq2sam-long", "maq2sam-short": "/usr/local/bin/maq2sam-short", "md5fa": "/usr/local/bin/md5fa", "md5sum-lite": "/usr/local/bin/md5sum-lite", "plot-bamstats": "/usr/local/bin/plot-bamstats", "psl2sam.pl": "/usr/local/bin/psl2sam.pl", "sam2vcf.pl": "/usr/local/bin/sam2vcf.pl", "samtools.pl": "/usr/local/bin/samtools.pl", "seq_cache_populate.pl": "/usr/local/bin/seq_cache_populate.pl", "soap2sam.pl": "/usr/local/bin/soap2sam.pl", "zoom2sam.pl": "/usr/local/bin/zoom2sam.pl", "novo2sam.pl": "/usr/local/bin/novo2sam.pl", "wgsim": "/usr/local/bin/wgsim", "wgsim_eval.pl": "/usr/local/bin/wgsim_eval.pl", "samtools": "/usr/local/bin/samtools", "htsfile": "/usr/local/bin/htsfile", "bgzip": "/usr/local/bin/bgzip", "tabix": "/usr/local/bin/tabix"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/debreak.
singularity registry hpc automated addition for debreak
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/debreak
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/debreak:1.3--h9ee0642_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/debreak/1.3--h9ee0642_0
$ module help quay.io/biocontainers/debreak/1.3--h9ee0642_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### debreak-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### debreak-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### debreak-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### debreak-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### debreak-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### debreak-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### bsalign

```bash
$ singularity exec <container> /usr/local/bin/bsalign
$ podman run --it --rm --entrypoint /usr/local/bin/bsalign   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bsalign   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### complexsv.py

```bash
$ singularity exec <container> /usr/local/bin/complexsv.py
$ podman run --it --rm --entrypoint /usr/local/bin/complexsv.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/complexsv.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### debreak

```bash
$ singularity exec <container> /usr/local/bin/debreak
$ podman run --it --rm --entrypoint /usr/local/bin/debreak   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/debreak   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### debreak_allpoa.py

```bash
$ singularity exec <container> /usr/local/bin/debreak_allpoa.py
$ podman run --it --rm --entrypoint /usr/local/bin/debreak_allpoa.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/debreak_allpoa.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### debreak_detect.py

```bash
$ singularity exec <container> /usr/local/bin/debreak_detect.py
$ podman run --it --rm --entrypoint /usr/local/bin/debreak_detect.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/debreak_detect.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### debreak_genotype.py

```bash
$ singularity exec <container> /usr/local/bin/debreak_genotype.py
$ podman run --it --rm --entrypoint /usr/local/bin/debreak_genotype.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/debreak_genotype.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### debreak_merge.py

```bash
$ singularity exec <container> /usr/local/bin/debreak_merge.py
$ podman run --it --rm --entrypoint /usr/local/bin/debreak_merge.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/debreak_merge.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### debreak_merge_cluster.py

```bash
$ singularity exec <container> /usr/local/bin/debreak_merge_cluster.py
$ podman run --it --rm --entrypoint /usr/local/bin/debreak_merge_cluster.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/debreak_merge_cluster.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### debreak_merge_contig.py

```bash
$ singularity exec <container> /usr/local/bin/debreak_merge_contig.py
$ podman run --it --rm --entrypoint /usr/local/bin/debreak_merge_contig.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/debreak_merge_contig.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### debreak_rescuedupfromins.py

```bash
$ singularity exec <container> /usr/local/bin/debreak_rescuedupfromins.py
$ podman run --it --rm --entrypoint /usr/local/bin/debreak_rescuedupfromins.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/debreak_rescuedupfromins.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### debreak_rescuelargeins.py

```bash
$ singularity exec <container> /usr/local/bin/debreak_rescuelargeins.py
$ podman run --it --rm --entrypoint /usr/local/bin/debreak_rescuelargeins.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/debreak_rescuelargeins.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### debreak_resdup_selfalignment.py

```bash
$ singularity exec <container> /usr/local/bin/debreak_resdup_selfalignment.py
$ podman run --it --rm --entrypoint /usr/local/bin/debreak_resdup_selfalignment.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/debreak_resdup_selfalignment.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### debreak_writevcf.py

```bash
$ singularity exec <container> /usr/local/bin/debreak_writevcf.py
$ podman run --it --rm --entrypoint /usr/local/bin/debreak_writevcf.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/debreak_writevcf.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### genefusion.py

```bash
$ singularity exec <container> /usr/local/bin/genefusion.py
$ podman run --it --rm --entrypoint /usr/local/bin/genefusion.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/genefusion.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### wtdbg-cns

```bash
$ singularity exec <container> /usr/local/bin/wtdbg-cns
$ podman run --it --rm --entrypoint /usr/local/bin/wtdbg-cns   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/wtdbg-cns   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### wtdbg2

```bash
$ singularity exec <container> /usr/local/bin/wtdbg2
$ podman run --it --rm --entrypoint /usr/local/bin/wtdbg2   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/wtdbg2   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### wtpoa-cns

```bash
$ singularity exec <container> /usr/local/bin/wtpoa-cns
$ podman run --it --rm --entrypoint /usr/local/bin/wtpoa-cns   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/wtpoa-cns   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### paftools.js

```bash
$ singularity exec <container> /usr/local/bin/paftools.js
$ podman run --it --rm --entrypoint /usr/local/bin/paftools.js   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/paftools.js   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### minimap2

```bash
$ singularity exec <container> /usr/local/bin/minimap2
$ podman run --it --rm --entrypoint /usr/local/bin/minimap2   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/minimap2   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ace2sam

```bash
$ singularity exec <container> /usr/local/bin/ace2sam
$ podman run --it --rm --entrypoint /usr/local/bin/ace2sam   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ace2sam   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### blast2sam.pl

```bash
$ singularity exec <container> /usr/local/bin/blast2sam.pl
$ podman run --it --rm --entrypoint /usr/local/bin/blast2sam.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/blast2sam.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bowtie2sam.pl

```bash
$ singularity exec <container> /usr/local/bin/bowtie2sam.pl
$ podman run --it --rm --entrypoint /usr/local/bin/bowtie2sam.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bowtie2sam.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### export2sam.pl

```bash
$ singularity exec <container> /usr/local/bin/export2sam.pl
$ podman run --it --rm --entrypoint /usr/local/bin/export2sam.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/export2sam.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### interpolate_sam.pl

```bash
$ singularity exec <container> /usr/local/bin/interpolate_sam.pl
$ podman run --it --rm --entrypoint /usr/local/bin/interpolate_sam.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/interpolate_sam.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### maq2sam-long

```bash
$ singularity exec <container> /usr/local/bin/maq2sam-long
$ podman run --it --rm --entrypoint /usr/local/bin/maq2sam-long   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/maq2sam-long   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### maq2sam-short

```bash
$ singularity exec <container> /usr/local/bin/maq2sam-short
$ podman run --it --rm --entrypoint /usr/local/bin/maq2sam-short   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/maq2sam-short   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### md5fa

```bash
$ singularity exec <container> /usr/local/bin/md5fa
$ podman run --it --rm --entrypoint /usr/local/bin/md5fa   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/md5fa   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### md5sum-lite

```bash
$ singularity exec <container> /usr/local/bin/md5sum-lite
$ podman run --it --rm --entrypoint /usr/local/bin/md5sum-lite   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/md5sum-lite   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### plot-bamstats

```bash
$ singularity exec <container> /usr/local/bin/plot-bamstats
$ podman run --it --rm --entrypoint /usr/local/bin/plot-bamstats   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/plot-bamstats   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### psl2sam.pl

```bash
$ singularity exec <container> /usr/local/bin/psl2sam.pl
$ podman run --it --rm --entrypoint /usr/local/bin/psl2sam.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/psl2sam.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### sam2vcf.pl

```bash
$ singularity exec <container> /usr/local/bin/sam2vcf.pl
$ podman run --it --rm --entrypoint /usr/local/bin/sam2vcf.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/sam2vcf.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### samtools.pl

```bash
$ singularity exec <container> /usr/local/bin/samtools.pl
$ podman run --it --rm --entrypoint /usr/local/bin/samtools.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/samtools.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### seq_cache_populate.pl

```bash
$ singularity exec <container> /usr/local/bin/seq_cache_populate.pl
$ podman run --it --rm --entrypoint /usr/local/bin/seq_cache_populate.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/seq_cache_populate.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### soap2sam.pl

```bash
$ singularity exec <container> /usr/local/bin/soap2sam.pl
$ podman run --it --rm --entrypoint /usr/local/bin/soap2sam.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/soap2sam.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### zoom2sam.pl

```bash
$ singularity exec <container> /usr/local/bin/zoom2sam.pl
$ podman run --it --rm --entrypoint /usr/local/bin/zoom2sam.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/zoom2sam.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### novo2sam.pl

```bash
$ singularity exec <container> /usr/local/bin/novo2sam.pl
$ podman run --it --rm --entrypoint /usr/local/bin/novo2sam.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/novo2sam.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### wgsim

```bash
$ singularity exec <container> /usr/local/bin/wgsim
$ podman run --it --rm --entrypoint /usr/local/bin/wgsim   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/wgsim   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### wgsim_eval.pl

```bash
$ singularity exec <container> /usr/local/bin/wgsim_eval.pl
$ podman run --it --rm --entrypoint /usr/local/bin/wgsim_eval.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/wgsim_eval.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### samtools

```bash
$ singularity exec <container> /usr/local/bin/samtools
$ podman run --it --rm --entrypoint /usr/local/bin/samtools   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/samtools   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### htsfile

```bash
$ singularity exec <container> /usr/local/bin/htsfile
$ podman run --it --rm --entrypoint /usr/local/bin/htsfile   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/htsfile   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bgzip

```bash
$ singularity exec <container> /usr/local/bin/bgzip
$ podman run --it --rm --entrypoint /usr/local/bin/bgzip   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bgzip   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### tabix

```bash
$ singularity exec <container> /usr/local/bin/tabix
$ podman run --it --rm --entrypoint /usr/local/bin/tabix   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/tabix   -v ${PWD} -w ${PWD} <container> -c " $@"
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