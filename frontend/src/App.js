import "./App.css";
import { useState, useEffect } from "react";

function App() {
	const [languages, setLanguages] = useState(undefined);

	useEffect(() => {
		fetch("http://localhost/languages")
			.then((response) => response.json())
			.then((json) => {
				setLanguages(json.data);
			});
	}, []);

	return (
		<div className="App">
			<header className="App-header">
				<p>React with Flask API on Docker</p>
				{languages ? (
					<ul>
						{languages.map((lang) => {
							return <li>{lang.name}</li>;
						})}
					</ul>
				) : (
					<></>
				)}
			</header>
		</div>
	);
}

export default App;
