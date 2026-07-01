export default function StatsCard({title,value,color}){

    return(

        <div className="bg-slate-800 rounded-xl shadow-lg p-6 flex-1">

            <p className="text-gray-400">

                {title}

            </p>

            <h1
            className="text-4xl font-bold mt-3"
            style={{color}}
            >

                {value}

            </h1>

        </div>

    )

}