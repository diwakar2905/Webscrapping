html='''
<div class="col-md-4 col-xl-4 col-lg-4">
    <div class="card thumbnail" itemscope itemtype="https://schema.org/Product">
        <div class="product-wrapper card-body">
            <img class="img-fluid card-img-top image img-responsive" alt="item" src="/images/test-sites/e-commerce/items/cart2.png" itemprop="image">
            <div class="caption">
                <h4 class="price float-end card-title pull-right" itemprop="offers" itemscope itemtype="https://schema.org/Offer">
                    <span itemprop="price">$1102.66</span>
                    <meta itemprop="priceCurrency" content="USD">
                </h4>
                <h4>
                    <a href="/test-sites/e-commerce/allinone/product/99" class="title" title="Dell Latitude 5280" itemprop="name">
                        Dell Latitude...
                    </a>
                </h4>
                <p class="description card-text" itemprop="description">Dell Latitude 5280, 12.5&quot; HD, Core i5-7300U, 8GB, 256GB SSD, Windows 10 Pro</p>

            </div>
            <div class="ratings" itemprop="aggregateRating" itemscope itemtype="https://schema.org/AggregateRating">
                <p class="review-count float-end">
                    <span itemprop="reviewCount">8</span> reviews
                </p>
                <p data-rating="1">
                                        <span class="ws-icon ws-icon-star"></span>
                                    </p>
            </div>
        </div>
    </div>
</div>
<div class="col-md-4 col-xl-4 col-lg-4">
    <div class="card thumbnail" itemscope itemtype="https://schema.org/Product">
        <div class="product-wrapper card-body">
            <img class="img-fluid card-img-top image img-responsive" alt="item" src="/images/test-sites/e-commerce/items/cart2.png" itemprop="image">
            <div class="caption">
                <h4 class="price float-end card-title pull-right" itemprop="offers" itemscope itemtype="https://schema.org/Offer">
                    <span itemprop="price">$1326.83</span>
                    <meta itemprop="priceCurrency" content="USD">
                </h4>
                <h4>
                    <a href="/test-sites/e-commerce/allinone/product/137" class="title" title="Hewlett Packard ProBook 640 G3" itemprop="name">
                        Hewlett Packar...
                    </a>
                </h4>
                <p class="description card-text" itemprop="description">Hewlett Packard ProBook 640 G3, 14&quot; FHD, Core i7-7600U, 8GB, 256GB SSD, Windows 10 Pro</p>

            </div>
            <div class="ratings" itemprop="aggregateRating" itemscope itemtype="https://schema.org/AggregateRating">
                <p class="review-count float-end">
                    <span itemprop="reviewCount">12</span> reviews
                </p>
                <p data-rating="1">
                                        <span class="ws-icon ws-icon-star"></span>
                                    </p>
            </div>
        </div>
    </div>
</div>
'''
from bs4 import BeautifulSoup
soup = BeautifulSoup(html, "html.parser")

# Sare product cards dhundh rahe hain
for prod in soup.find_all("div", class_="col-md-4 col-xl-4 col-lg-4"):
    # Price nikal rahe hain
    price_tag = prod.find("span", itemprop="price")
    # Description nikal rahe hain
    description_tag = prod.find("p", class_="description")
    # Rating (number of reviews) nikal rahe hain
    rating_tag = prod.find("p", class_="review-count")
    
    price = price_tag.text.strip() if price_tag else "N/A"
    description = description_tag.text.strip() if description_tag else "N/A"
    # Sirf review count nikal rahe hain, pura text nahi
    rating = rating_tag.find("span", itemprop="reviewCount").text.strip() if rating_tag and rating_tag.find("span", itemprop="reviewCount") else "N/A"
    
    print(f"Price: {price}")
    print(f"Description: {description}")
    print(f"Rating: {rating}")
    print("-" * 40)  # Alag alag products ko separate dikhane