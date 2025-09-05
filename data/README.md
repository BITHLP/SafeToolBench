## Some examples of SafeToolBench
SafeToolBench is saved in JSON format, which includes the following fields:

> ***instruction***: Stores the specific risky instruction.
>
> ***risk category***: Stores the risk category corresponding to the instruction.
>
> ***explanation***: Provides a detailed explanation of why the instruction is risky.
> ***output***: Stores the tool planning calls corresponding to the instruction.
> > ***used_app***: Stores the list of APPs used by the instruction.
> 
> > ***used_api***: Stores the APIs used in the corresponding APPs.
> > > ***api_i***: Stores the detailed keys and values of the APIs used.
> >
> > > ***use_times***: Stores the number of times the API needs to be used to complete the instruction.
>
> ***quality_score*** : Stores the quality control score for each instruction, evaluated by GPT-4.