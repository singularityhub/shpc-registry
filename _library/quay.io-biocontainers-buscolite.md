---
layout: container
name:  "quay.io/biocontainers/buscolite"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/buscolite/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/buscolite/container.yaml"
updated_at: "2026-01-31 04:41:00.650574"
latest: "25.4.24--pyhdfd78af_0"
container_url: "https://biocontainers.pro/tools/buscolite"
aliases:
 - "PF00225_full.blocks.txt"
 - "PF00225_seed.blocks.txt"
 - "add_name_to_gff3.pl"
 - "aln2wig"
 - "augustify.py"
 - "buscolite"
 - "executeTestCGP.py"
 - "extractAnno.py"
 - "findRepetitiveProtSeqs.py"
 - "get_loci_from_gb.pl"
 - "miniprot"
 - "pp_simScore"
 - "rename_species.pl"
 - "stringtie2fa.py"
 - "bamToWig.py"
 - "compare_masking.pl"
 - "fix_in_frame_stop_codon_genes.py"
 - "fix_joingenes_gtf.pl"
 - "merge_masking.pl"
 - "aa2nonred.pl"
 - "cdbfasta"
 - "cdbyank"
 - "compileSpliceCands"
 - "computeFlankingRegion.pl"
 - "eval_multi_gtf.pl"
 - "filterGenesIn.pl"
 - "findGffNamesInFasta.pl"
 - "getAnnoFastaFromJoingenes.py"
 - "getLinesMatching.pl"
 - "gtf2aa.pl"
 - "gth2gtf.pl"
 - "setStopCodonFreqs.pl"
 - "utrrnaseq"
 - "SplicedAlignment.pm"
 - "augustus2browser.pl"
 - "augustus2gbrowse.pl"
 - "autoAug.pl"
 - "autoAugPred.pl"
 - "autoAugTrain.pl"
versions:
 - "23.10.26--pyhdfd78af_0"
 - "24.11.3--pyhdfd78af_0"
 - "25.4.24--pyhdfd78af_0"
description: "singularity registry hpc automated addition for buscolite"
config: {"url": "https://biocontainers.pro/tools/buscolite", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for buscolite", "latest": {"25.4.24--pyhdfd78af_0": "sha256:09489b2a9db8b8dcc19d88423677d74b3de06bad0198f8bd541413e3b2f5701b"}, "tags": {"23.10.26--pyhdfd78af_0": "sha256:eaa3ed539c8e98e8a31e503d63b7242a5772116a237b167c3d7bc6916de2ea7a", "24.11.3--pyhdfd78af_0": "sha256:cee024cf6effb9de5ae5cd247ec7c7bf2f0cee4147f13a2ed77562e55178ca43", "25.4.24--pyhdfd78af_0": "sha256:09489b2a9db8b8dcc19d88423677d74b3de06bad0198f8bd541413e3b2f5701b"}, "docker": "quay.io/biocontainers/buscolite", "aliases": {"PF00225_full.blocks.txt": "/usr/local/bin/PF00225_full.blocks.txt", "PF00225_seed.blocks.txt": "/usr/local/bin/PF00225_seed.blocks.txt", "add_name_to_gff3.pl": "/usr/local/bin/add_name_to_gff3.pl", "aln2wig": "/usr/local/bin/aln2wig", "augustify.py": "/usr/local/bin/augustify.py", "buscolite": "/usr/local/bin/buscolite", "executeTestCGP.py": "/usr/local/bin/executeTestCGP.py", "extractAnno.py": "/usr/local/bin/extractAnno.py", "findRepetitiveProtSeqs.py": "/usr/local/bin/findRepetitiveProtSeqs.py", "get_loci_from_gb.pl": "/usr/local/bin/get_loci_from_gb.pl", "miniprot": "/usr/local/bin/miniprot", "pp_simScore": "/usr/local/bin/pp_simScore", "rename_species.pl": "/usr/local/bin/rename_species.pl", "stringtie2fa.py": "/usr/local/bin/stringtie2fa.py", "bamToWig.py": "/usr/local/bin/bamToWig.py", "compare_masking.pl": "/usr/local/bin/compare_masking.pl", "fix_in_frame_stop_codon_genes.py": "/usr/local/bin/fix_in_frame_stop_codon_genes.py", "fix_joingenes_gtf.pl": "/usr/local/bin/fix_joingenes_gtf.pl", "merge_masking.pl": "/usr/local/bin/merge_masking.pl", "aa2nonred.pl": "/usr/local/bin/aa2nonred.pl", "cdbfasta": "/usr/local/bin/cdbfasta", "cdbyank": "/usr/local/bin/cdbyank", "compileSpliceCands": "/usr/local/bin/compileSpliceCands", "computeFlankingRegion.pl": "/usr/local/bin/computeFlankingRegion.pl", "eval_multi_gtf.pl": "/usr/local/bin/eval_multi_gtf.pl", "filterGenesIn.pl": "/usr/local/bin/filterGenesIn.pl", "findGffNamesInFasta.pl": "/usr/local/bin/findGffNamesInFasta.pl", "getAnnoFastaFromJoingenes.py": "/usr/local/bin/getAnnoFastaFromJoingenes.py", "getLinesMatching.pl": "/usr/local/bin/getLinesMatching.pl", "gtf2aa.pl": "/usr/local/bin/gtf2aa.pl", "gth2gtf.pl": "/usr/local/bin/gth2gtf.pl", "setStopCodonFreqs.pl": "/usr/local/bin/setStopCodonFreqs.pl", "utrrnaseq": "/usr/local/bin/utrrnaseq", "SplicedAlignment.pm": "/usr/local/bin/SplicedAlignment.pm", "augustus2browser.pl": "/usr/local/bin/augustus2browser.pl", "augustus2gbrowse.pl": "/usr/local/bin/augustus2gbrowse.pl", "autoAug.pl": "/usr/local/bin/autoAug.pl", "autoAugPred.pl": "/usr/local/bin/autoAugPred.pl", "autoAugTrain.pl": "/usr/local/bin/autoAugTrain.pl"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/buscolite.
singularity registry hpc automated addition for buscolite
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/buscolite
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/buscolite:25.4.24--pyhdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/buscolite/25.4.24--pyhdfd78af_0
$ module help quay.io/biocontainers/buscolite/25.4.24--pyhdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### buscolite-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### buscolite-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### buscolite-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### buscolite-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### buscolite-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### buscolite-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### PF00225_full.blocks.txt

```bash
$ singularity exec <container> /usr/local/bin/PF00225_full.blocks.txt
$ podman run --it --rm --entrypoint /usr/local/bin/PF00225_full.blocks.txt   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/PF00225_full.blocks.txt   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### PF00225_seed.blocks.txt

```bash
$ singularity exec <container> /usr/local/bin/PF00225_seed.blocks.txt
$ podman run --it --rm --entrypoint /usr/local/bin/PF00225_seed.blocks.txt   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/PF00225_seed.blocks.txt   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### add_name_to_gff3.pl

```bash
$ singularity exec <container> /usr/local/bin/add_name_to_gff3.pl
$ podman run --it --rm --entrypoint /usr/local/bin/add_name_to_gff3.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/add_name_to_gff3.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### aln2wig

```bash
$ singularity exec <container> /usr/local/bin/aln2wig
$ podman run --it --rm --entrypoint /usr/local/bin/aln2wig   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/aln2wig   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### augustify.py

```bash
$ singularity exec <container> /usr/local/bin/augustify.py
$ podman run --it --rm --entrypoint /usr/local/bin/augustify.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/augustify.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### buscolite

```bash
$ singularity exec <container> /usr/local/bin/buscolite
$ podman run --it --rm --entrypoint /usr/local/bin/buscolite   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/buscolite   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### executeTestCGP.py

```bash
$ singularity exec <container> /usr/local/bin/executeTestCGP.py
$ podman run --it --rm --entrypoint /usr/local/bin/executeTestCGP.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/executeTestCGP.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### extractAnno.py

```bash
$ singularity exec <container> /usr/local/bin/extractAnno.py
$ podman run --it --rm --entrypoint /usr/local/bin/extractAnno.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/extractAnno.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### findRepetitiveProtSeqs.py

```bash
$ singularity exec <container> /usr/local/bin/findRepetitiveProtSeqs.py
$ podman run --it --rm --entrypoint /usr/local/bin/findRepetitiveProtSeqs.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/findRepetitiveProtSeqs.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### get_loci_from_gb.pl

```bash
$ singularity exec <container> /usr/local/bin/get_loci_from_gb.pl
$ podman run --it --rm --entrypoint /usr/local/bin/get_loci_from_gb.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/get_loci_from_gb.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### miniprot

```bash
$ singularity exec <container> /usr/local/bin/miniprot
$ podman run --it --rm --entrypoint /usr/local/bin/miniprot   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/miniprot   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pp_simScore

```bash
$ singularity exec <container> /usr/local/bin/pp_simScore
$ podman run --it --rm --entrypoint /usr/local/bin/pp_simScore   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pp_simScore   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### rename_species.pl

```bash
$ singularity exec <container> /usr/local/bin/rename_species.pl
$ podman run --it --rm --entrypoint /usr/local/bin/rename_species.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/rename_species.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### stringtie2fa.py

```bash
$ singularity exec <container> /usr/local/bin/stringtie2fa.py
$ podman run --it --rm --entrypoint /usr/local/bin/stringtie2fa.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/stringtie2fa.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bamToWig.py

```bash
$ singularity exec <container> /usr/local/bin/bamToWig.py
$ podman run --it --rm --entrypoint /usr/local/bin/bamToWig.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bamToWig.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### compare_masking.pl

```bash
$ singularity exec <container> /usr/local/bin/compare_masking.pl
$ podman run --it --rm --entrypoint /usr/local/bin/compare_masking.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/compare_masking.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fix_in_frame_stop_codon_genes.py

```bash
$ singularity exec <container> /usr/local/bin/fix_in_frame_stop_codon_genes.py
$ podman run --it --rm --entrypoint /usr/local/bin/fix_in_frame_stop_codon_genes.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fix_in_frame_stop_codon_genes.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fix_joingenes_gtf.pl

```bash
$ singularity exec <container> /usr/local/bin/fix_joingenes_gtf.pl
$ podman run --it --rm --entrypoint /usr/local/bin/fix_joingenes_gtf.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fix_joingenes_gtf.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### merge_masking.pl

```bash
$ singularity exec <container> /usr/local/bin/merge_masking.pl
$ podman run --it --rm --entrypoint /usr/local/bin/merge_masking.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/merge_masking.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### aa2nonred.pl

```bash
$ singularity exec <container> /usr/local/bin/aa2nonred.pl
$ podman run --it --rm --entrypoint /usr/local/bin/aa2nonred.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/aa2nonred.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### cdbfasta

```bash
$ singularity exec <container> /usr/local/bin/cdbfasta
$ podman run --it --rm --entrypoint /usr/local/bin/cdbfasta   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cdbfasta   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### cdbyank

```bash
$ singularity exec <container> /usr/local/bin/cdbyank
$ podman run --it --rm --entrypoint /usr/local/bin/cdbyank   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cdbyank   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### compileSpliceCands

```bash
$ singularity exec <container> /usr/local/bin/compileSpliceCands
$ podman run --it --rm --entrypoint /usr/local/bin/compileSpliceCands   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/compileSpliceCands   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### computeFlankingRegion.pl

```bash
$ singularity exec <container> /usr/local/bin/computeFlankingRegion.pl
$ podman run --it --rm --entrypoint /usr/local/bin/computeFlankingRegion.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/computeFlankingRegion.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### eval_multi_gtf.pl

```bash
$ singularity exec <container> /usr/local/bin/eval_multi_gtf.pl
$ podman run --it --rm --entrypoint /usr/local/bin/eval_multi_gtf.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/eval_multi_gtf.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### filterGenesIn.pl

```bash
$ singularity exec <container> /usr/local/bin/filterGenesIn.pl
$ podman run --it --rm --entrypoint /usr/local/bin/filterGenesIn.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/filterGenesIn.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### findGffNamesInFasta.pl

```bash
$ singularity exec <container> /usr/local/bin/findGffNamesInFasta.pl
$ podman run --it --rm --entrypoint /usr/local/bin/findGffNamesInFasta.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/findGffNamesInFasta.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### getAnnoFastaFromJoingenes.py

```bash
$ singularity exec <container> /usr/local/bin/getAnnoFastaFromJoingenes.py
$ podman run --it --rm --entrypoint /usr/local/bin/getAnnoFastaFromJoingenes.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/getAnnoFastaFromJoingenes.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### getLinesMatching.pl

```bash
$ singularity exec <container> /usr/local/bin/getLinesMatching.pl
$ podman run --it --rm --entrypoint /usr/local/bin/getLinesMatching.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/getLinesMatching.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gtf2aa.pl

```bash
$ singularity exec <container> /usr/local/bin/gtf2aa.pl
$ podman run --it --rm --entrypoint /usr/local/bin/gtf2aa.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gtf2aa.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gth2gtf.pl

```bash
$ singularity exec <container> /usr/local/bin/gth2gtf.pl
$ podman run --it --rm --entrypoint /usr/local/bin/gth2gtf.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gth2gtf.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### setStopCodonFreqs.pl

```bash
$ singularity exec <container> /usr/local/bin/setStopCodonFreqs.pl
$ podman run --it --rm --entrypoint /usr/local/bin/setStopCodonFreqs.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/setStopCodonFreqs.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### utrrnaseq

```bash
$ singularity exec <container> /usr/local/bin/utrrnaseq
$ podman run --it --rm --entrypoint /usr/local/bin/utrrnaseq   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/utrrnaseq   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### SplicedAlignment.pm

```bash
$ singularity exec <container> /usr/local/bin/SplicedAlignment.pm
$ podman run --it --rm --entrypoint /usr/local/bin/SplicedAlignment.pm   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/SplicedAlignment.pm   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### augustus2browser.pl

```bash
$ singularity exec <container> /usr/local/bin/augustus2browser.pl
$ podman run --it --rm --entrypoint /usr/local/bin/augustus2browser.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/augustus2browser.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### augustus2gbrowse.pl

```bash
$ singularity exec <container> /usr/local/bin/augustus2gbrowse.pl
$ podman run --it --rm --entrypoint /usr/local/bin/augustus2gbrowse.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/augustus2gbrowse.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### autoAug.pl

```bash
$ singularity exec <container> /usr/local/bin/autoAug.pl
$ podman run --it --rm --entrypoint /usr/local/bin/autoAug.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/autoAug.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### autoAugPred.pl

```bash
$ singularity exec <container> /usr/local/bin/autoAugPred.pl
$ podman run --it --rm --entrypoint /usr/local/bin/autoAugPred.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/autoAugPred.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### autoAugTrain.pl

```bash
$ singularity exec <container> /usr/local/bin/autoAugTrain.pl
$ podman run --it --rm --entrypoint /usr/local/bin/autoAugTrain.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/autoAugTrain.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
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