async function gql(query, variables={}) {
    const data = await fetch('https://api.hashnode.com/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({
            query,
            variables
        })
    });

    return data.json();
}

const GET_USER_ARTICLES = `
    query GetUserArticles($page: Int!) {
        user(username: "catalinpit") {
            publication {
                posts(page: $page) {
                    title
                    brief
                    slug
                    coverImage
                }
            }
        }
    }
`;
gql(GET_USER_ARTICLES, { page: 0 })
    .then(result => {
        const articles = result.data.user.publication.posts;
        let container = document.createElement('div');
        container.className="bcard bcard1"

        articles.forEach(article => {
            let title = document.createElement('h2');
            title.innerText = article.title;
            title.className="title"

            let brief = document.createElement('p');
            brief.innerText = article.brief;
            brief.className="bcard-body"

            let img =document.createElement('img');
            img.className="featured-image"
            img.src = article.coverImage

            let link = document.createElement('a');
            link.className = "more-bottun";
            link.innerText = 'Read more...';
            link.href = `https://catalins.tech/${article.slug}`;

            container.appendChild(title);
            container.appendChild(brief);
            container.appendChild(link);
            container.appendChild(img);
        })

        document.getElementById('articles').appendChild(container);
});

document.getElementById('articles').parentNode.innerHTML = `
    <h1 class="section-title">Catalin Pit's Articles</h1>
`;


